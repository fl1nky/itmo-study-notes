"""Move confirmed finished deadlines to the archive; keep overdue work visible."""

from __future__ import annotations

import argparse
import re
import tempfile
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parents[1]
ACTIVE = ROOT / "ДЕДЛАЙНЫ.md"
ARCHIVE = ROOT / "архив" / "ДЕДЛАЙНЫ.md"
START = "<!-- DEADLINES:START -->"
END = "<!-- DEADLINES:END -->"
OPEN_STATUSES = {"TODO", "IN_PROGRESS", "BLOCKED"}
CLOSED_STATUSES = {"DONE", "CANCELLED"}
ACTIVE_HEADER = "| ID | Дисциплина | Дата | Задача | Статус | Источник и уточнение | Пометка |"
ARCHIVE_HEADER = "| ID | Дисциплина | Дата | Задача | Итог | Источник и уточнение | Перенесено (МСК) | Причина |"


@dataclass(frozen=True)
class Deadline:
    item_id: str
    course: str
    due: str
    task: str
    status: str
    source: str
    freshness: str = ""


def split_row(line: str, count: int) -> list[str]:
    if not line.startswith("|") or not line.endswith("|"):
        raise ValueError(f"Неверная строка таблицы: {line}")
    cells = [cell.strip().replace(r"\|", "|") for cell in re.split(r"(?<!\\)\|", line)[1:-1]]
    if len(cells) != count:
        raise ValueError(f"Ожидалось {count} колонок, получено {len(cells)}: {line}")
    return cells


def read_table(path: Path, header: str, columns: int) -> tuple[str, list[list[str]]]:
    content = path.read_text(encoding="utf-8")
    if content.count(START) != 1 or content.count(END) != 1:
        raise ValueError(f"Ожидалась одна таблица дедлайнов в {path}")
    body = content.split(START, 1)[1].split(END, 1)[0]
    lines = [line.strip() for line in body.splitlines() if line.strip()]
    if len(lines) < 2 or lines[0] != header:
        raise ValueError(f"Заголовок таблицы изменён в {path}")
    separator = split_row(lines[1], columns)
    if any(not re.fullmatch(r":?-{3,}:?", cell) for cell in separator):
        raise ValueError(f"Неверный разделитель таблицы в {path}")
    return content, [split_row(line, columns) for line in lines[2:]]


def cell_text(value: str) -> str:
    if "\n" in value or "\r" in value:
        raise ValueError("Ячейка таблицы не может содержать перенос строки")
    return value.replace("|", r"\|")


def replace_table(content: str, header: str, rows: list[list[str]]) -> str:
    before, rest = content.split(START, 1)
    _, after = rest.split(END, 1)
    width = header.count("|") - 1
    separator = "|" + "---|" * width
    rendered = [header, separator]
    rendered.extend("| " + " | ".join(cell_text(cell) for cell in row) + " |" for row in rows)
    return before + START + "\n" + "\n".join(rendered) + "\n" + END + after


def validate_due(value: str) -> date | None:
    if value == "неизвестна":
        return None
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        raise ValueError(f"Дата должна быть YYYY-MM-DD или «неизвестна»: {value}")
    return date.fromisoformat(value)


def freshness(due: date | None, today: date) -> str:
    if due is None:
        return "уточнить дату"
    if due < today:
        return "просрочен"
    if due == today:
        return "сегодня"
    return "впереди"


def atomic_write(path: Path, content: str) -> bool:
    if path.read_text(encoding="utf-8") == content:
        return False
    with tempfile.NamedTemporaryFile(
        mode="w", encoding="utf-8", newline="\n", dir=path.parent, prefix=".deadlines-", delete=False
    ) as handle:
        handle.write(content)
        temporary = Path(handle.name)
    temporary.replace(path)
    return True


def sync(active_path: Path = ACTIVE, archive_path: Path = ARCHIVE, today: date | None = None) -> tuple[int, bool]:
    today = today or datetime.now(ZoneInfo("Europe/Moscow")).date()
    active_text, active_rows = read_table(active_path, ACTIVE_HEADER, 7)
    archive_text, archive_rows = read_table(archive_path, ARCHIVE_HEADER, 8)
    archived_ids = {row[0] for row in archive_rows}
    if len(archived_ids) != len(archive_rows):
        raise ValueError("Повторяющийся ID в архиве")

    seen: set[str] = set()
    keep: list[Deadline] = []
    moved = 0
    for row in active_rows:
        item = Deadline(*row)
        if not item.item_id or not item.course or not item.task or not item.source:
            raise ValueError(f"Незаполненная обязательная ячейка у {item.item_id or 'строки без ID'}")
        if item.item_id in seen:
            raise ValueError(f"Повторяющийся ID в текущих дедлайнах: {item.item_id}")
        seen.add(item.item_id)
        due = validate_due(item.due)
        if item.status not in OPEN_STATUSES | CLOSED_STATUSES:
            raise ValueError(f"Неизвестный статус у {item.item_id}: {item.status}")
        if item.status in CLOSED_STATUSES:
            # A previous interrupted run may have written the archive first.
            if item.item_id not in archived_ids:
                reason = "выполнено" if item.status == "DONE" else "отменено"
                archive_rows.append([
                    item.item_id, item.course, item.due, item.task, item.status,
                    item.source, today.isoformat(), reason,
                ])
                archived_ids.add(item.item_id)
                moved += 1
            continue
        if item.item_id in archived_ids:
            raise ValueError(f"Открытый пункт {item.item_id} уже есть в архиве")
        keep.append(Deadline(item.item_id, item.course, item.due, item.task,
                             item.status, item.source, freshness(due, today)))

    keep.sort(key=lambda item: (validate_due(item.due) is None,
                                validate_due(item.due) or date.max,
                                item.course.casefold(), item.item_id))
    new_active = replace_table(active_text, ACTIVE_HEADER, [list(item.__dict__.values()) for item in keep])
    new_archive = replace_table(archive_text, ARCHIVE_HEADER, archive_rows)
    # Writing the archive first makes an interrupted run recoverable on retry.
    changed_archive = atomic_write(archive_path, new_archive)
    changed_active = atomic_write(active_path, new_active)
    return moved, changed_archive or changed_active


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--today", type=date.fromisoformat, help="Дата для проверки (YYYY-MM-DD); по умолчанию сегодня в Москве")
    args = parser.parse_args()
    moved, changed = sync(today=args.today)
    print(f"Перенесено в архив: {moved}; файлы изменены: {'да' if changed else 'нет'}")


if __name__ == "__main__":
    main()
