"""Create a dated lesson and rebuild its course index."""

from __future__ import annotations

import argparse
import re
from datetime import date
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
FOLDER_PATTERN = re.compile(r"^(\d{4}-\d{2}-\d{2}) \((.+)\)$")


def safe_topic(topic: str) -> str:
    topic = " ".join(topic.strip().split())
    if not topic or re.search(r'[<>:"/\\|?*\x00-\x1f]', topic):
        raise ValueError("Тема пуста или содержит символы, недопустимые в имени папки Windows")
    if topic.endswith(".") or topic.endswith(" "):
        raise ValueError("Тема не должна заканчиваться точкой или пробелом")
    if len(topic) > 100:
        raise ValueError("Сократите тему до 100 символов")
    return topic


def update_index(course: str) -> None:
    course_dir = ROOT / "дисциплины" / COURSES[course]
    index_path = course_dir / "README.md"
    content = index_path.read_text(encoding="utf-8")
    if content.count(START) != 1 or content.count(END) != 1:
        raise ValueError(f"В индексе {index_path} нет маркеров списка занятий")
    lessons: list[tuple[str, str, Path]] = []
    for note in (course_dir / "лекции").glob("*/конспект.md"):
        match = FOLDER_PATTERN.fullmatch(note.parent.name)
        if not match:
            raise ValueError(f"Неожиданное имя папки занятия: {note.parent.name}")
        date.fromisoformat(match.group(1))
        lessons.append((match.group(1), match.group(2), note))
    lessons.sort(key=lambda value: (value[0], value[1].casefold()))
    if lessons:
        rows = ["| Дата | Тема | Конспект и материалы |", "|---|---|---|"]
        for lesson_date, topic, note in lessons:
            relative = quote(note.relative_to(course_dir).as_posix(), safe="/")
            rows.append(f"| {lesson_date} | {topic.replace('|', r'\|')} | [Открыть]({relative}) |")
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
    folder = ROOT / "дисциплины" / COURSES[course_key] / "лекции" / f"{lesson_date.isoformat()} ({topic})"
    if folder.exists():
        raise FileExistsError(f"Занятие уже существует: {folder}")
    template = (ROOT / "ШАБЛОН_КОНСПЕКТА.md").read_text(encoding="utf-8")
    folder.mkdir(parents=True)
    note = folder / "конспект.md"
    for placeholder, value in {
        "{{DATE}}": lesson_date.isoformat(),
        "{{TOPIC}}": topic,
        "{{COURSE}}": COURSES[course_key],
        "{{KIND}}": kind,
    }.items():
        template = template.replace(placeholder, value)
    note.write_text(template, encoding="utf-8", newline="\n")
    update_index(course_key)
    return note


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--course", required=True, help="Русское название дисциплины или её короткий код")
    parser.add_argument("--date", required=True, type=date.fromisoformat)
    parser.add_argument("--topic", required=True)
    parser.add_argument("--kind", default="лекция", choices=["лекция", "практика", "семинар", "другое"])
    args = parser.parse_args()
    print(create_lesson(args.course, args.date, args.topic, args.kind))


if __name__ == "__main__":
    main()
