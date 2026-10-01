"""Create a dated lesson and rebuild its course index."""

from __future__ import annotations

import argparse
import re
from datetime import date, datetime
from pathlib import Path
from urllib.parse import quote


ROOT = Path(__file__).resolve().parents[1]
COURSES = {
    "dm": "Дискретная математика",
    "aisd": "Алгоритмы и структуры данных",
    "cpp": "Алгоритмическая практика на C++",
    "linal": "Линейная алгебра",
    "matan": "Математический анализ",
    "op": "Основы программирования",
    "ispro": "Инструментальные средства разработки ПО",
    "english": "Английский язык",
}
START = "<!-- LESSONS:START -->"
END = "<!-- LESSONS:END -->"
NOTE_PATTERN = re.compile(r"^(.+) \((\d{2}\.\d{2}\.\d{4})\)\.md$")
KIND_DIRECTORIES = {"лекция": "лекции", "практика": "практики", "семинар": "практики"}


def parse_lesson_date(value: str) -> date:
    """Accept the displayed date format and earlier ISO command arguments."""
    try:
        if re.fullmatch(r"\d{2}\.\d{2}\.\d{4}", value):
            return datetime.strptime(value, "%d.%m.%Y").date()
        return date.fromisoformat(value)
    except ValueError as error:
        raise ValueError("Дата должна быть ДД.ММ.ГГГГ или YYYY-MM-DD") from error


def safe_topic(topic: str) -> str:
    topic = " ".join(topic.strip().split())
    if not topic or re.search(r'[<>:"/\\|?*\x00-\x1f]', topic):
        raise ValueError("Тема пуста или содержит символы, недопустимые в имени папки Windows")
    if topic.endswith(".") or topic.endswith(" "):
        raise ValueError("Тема не должна заканчиваться точкой или пробелом")
    if len(topic) > 100:
        raise ValueError("Сократите тему до 100 символов")
    return topic


def lesson_directory(kind: str) -> str:
    try:
        return KIND_DIRECTORIES[kind]
    except KeyError as error:
        raise ValueError("Выберите вид занятия: лекция, практика или семинар") from error


def update_index(course: str, kind: str = "лекция") -> None:
    course_dir = ROOT / "дисциплины" / COURSES[course]
    folder = lesson_directory(kind)
    lesson_dir = course_dir / folder
    lesson_dir.mkdir(parents=True, exist_ok=True)
    index_path = lesson_dir / "README.md"
    if not index_path.exists():
        index_path.write_text(
            f"# {folder.capitalize()} — {COURSES[course]}\n\n"
            "Каждое занятие — отдельный файл `Тема (ДД.ММ.ГГГГ).md`.\n\n"
            f"## Занятия\n\n{START}\nПока занятий нет.\n{END}\n",
            encoding="utf-8", newline="\n",
        )
    content = index_path.read_text(encoding="utf-8")
    if content.count(START) != 1 or content.count(END) != 1:
        raise ValueError(f"В индексе {index_path} нет маркеров списка занятий")
    lessons: list[tuple[date, str, Path]] = []
    for note in lesson_dir.glob("*.md"):
        if note.name == "README.md":
            continue
        match = NOTE_PATTERN.fullmatch(note.name)
        if not match:
            raise ValueError(f"Неожиданное имя файла занятия: {note.name}")
        lessons.append((parse_lesson_date(match.group(2)), match.group(1), note))
    lessons.sort(key=lambda value: (value[0], value[1].casefold()))
    if lessons:
        rows = ["| Тема | Дата занятия | Конспект |", "|---|---|---|"]
        for lesson_date, topic, note in lessons:
            relative = quote(note.relative_to(lesson_dir).as_posix(), safe="/")
            rows.append(f"| {topic.replace('|', r'\|')} | {lesson_date:%d.%m.%Y} | [Открыть]({relative}) |")
        listing = "\n".join(rows)
    else:
        listing = "Пока занятий нет."
    before, rest = content.split(START, 1)
    _, after = rest.split(END, 1)
    index_path.write_text(before + START + "\n" + listing + "\n" + END + after, encoding="utf-8", newline="\n")


def create_lesson(course: str, lesson_date: date, topic: str, kind: str) -> Path:
    course_key = next((slug for slug, name in COURSES.items()
                       if course.casefold() in {slug.casefold(), name.casefold()}), None)
    if course_key is None:
        raise ValueError(f"Неизвестная дисциплина: {course}")
    topic = safe_topic(topic)
    lesson_dir = ROOT / "дисциплины" / COURSES[course_key] / lesson_directory(kind)
    note = lesson_dir / f"{topic} ({lesson_date:%d.%m.%Y}).md"
    if note.exists():
        raise FileExistsError(f"Занятие уже существует: {note}")
    template = (ROOT / "ШАБЛОН_КОНСПЕКТА.md").read_text(encoding="utf-8")
    lesson_dir.mkdir(parents=True, exist_ok=True)
    for placeholder, value in {
        "{{DATE}}": lesson_date.strftime("%d.%m.%Y"),
        "{{TOPIC}}": topic,
        "{{COURSE}}": COURSES[course_key],
    }.items():
        template = template.replace(placeholder, value)
    note.write_text(template, encoding="utf-8", newline="\n")
    update_index(course_key, kind)
    return note


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--course", required=True, help="Русское название дисциплины или её короткий код")
    parser.add_argument("--date", required=True, type=parse_lesson_date, help="Дата занятия: ДД.ММ.ГГГГ")
    parser.add_argument("--topic", required=True)
    parser.add_argument("--kind", default="лекция", choices=list(KIND_DIRECTORIES),
                        help="Лекция — в лекции; практика или семинар — в практики")
    args = parser.parse_args()
    print(create_lesson(args.course, args.date, args.topic, args.kind))


if __name__ == "__main__":
    main()
