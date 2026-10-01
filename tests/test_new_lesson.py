from __future__ import annotations

import tempfile
import unittest
from datetime import date
from pathlib import Path
from unittest.mock import patch
from urllib.parse import unquote
import re

from tools import new_lesson


class NewLessonTests(unittest.TestCase):
    def test_creates_dated_file_and_index(self) -> None:
        template = (new_lesson.ROOT / "ШАБЛОН_КОНСПЕКТА.md").read_text(encoding="utf-8")
        with tempfile.TemporaryDirectory() as temp, patch.object(new_lesson, "ROOT", Path(temp)):
            course = Path(temp) / "дисциплины" / "Дискретная математика" / "лекции"
            course.mkdir(parents=True)
            (course / "README.md").write_text(
                "# Дискретная математика\n<!-- LESSONS:START -->\nПока занятий нет.\n<!-- LESSONS:END -->\n",
                encoding="utf-8",
            )
            (Path(temp) / "ШАБЛОН_КОНСПЕКТА.md").write_text(
                template,
                encoding="utf-8",
            )
            note = new_lesson.create_lesson("Дискретная математика", date(2026, 9, 29), "Множества и операции", "лекция")
            self.assertEqual(note.parent, course)
            self.assertEqual(note.name, "Множества и операции (29.09.2026).md")
            content = note.read_text(encoding="utf-8")
            self.assertTrue(content.startswith("# Множества и операции\n"))
            self.assertIn("**Дата занятия:** 29.09.2026", content)
            self.assertNotIn("{{", content)
            self.assertEqual(content.count("<summary>Показать ответ</summary>"), 2)
            self.assertGreater(content.index("## Самое важное — теоретический минимум"), content.index("## Вопросы для самопроверки"))
            index = (course / "README.md").read_text(encoding="utf-8")
            self.assertIn("29.09.2026", index)
            self.assertIn("Множества и операции", index)
            with self.assertRaises(FileExistsError):
                new_lesson.create_lesson("dm", date(2026, 9, 29), "Множества и операции", "лекция")
            self.assertEqual(note.read_text(encoding="utf-8"), content)

    def test_index_sorts_calendar_dates_and_links_resolve(self) -> None:
        with tempfile.TemporaryDirectory() as temp, patch.object(new_lesson, "ROOT", Path(temp)):
            lectures = Path(temp) / "дисциплины" / "Дискретная математика" / "лекции"
            lectures.mkdir(parents=True)
            (lectures / "README.md").write_text(f"{new_lesson.START}\n{new_lesson.END}\n", encoding="utf-8")
            for name in ("Вторая тема (01.01.2026).md", "Первая тема (31.12.2025).md"):
                (lectures / name).write_text("# Тема\n", encoding="utf-8")
            new_lesson.update_index("dm")
            index = (lectures / "README.md").read_text(encoding="utf-8")
            self.assertLess(index.index("31.12.2025"), index.index("01.01.2026"))
            links = re.findall(r"\[Открыть\]\(([^)]+)\)", index)
            self.assertEqual(len(links), 2)
            for link in links:
                self.assertTrue((lectures / unquote(link)).is_file())

    def test_date_input_supports_display_and_existing_iso_format(self) -> None:
        self.assertEqual(new_lesson.parse_lesson_date("30.09.2026"), date(2026, 9, 30))
        self.assertEqual(new_lesson.parse_lesson_date("2026-09-30"), date(2026, 9, 30))
        with self.assertRaises(ValueError):
            new_lesson.parse_lesson_date("31.02.2026")

    def test_lecture_and_practice_with_same_topic_are_kept_separate(self) -> None:
        template = (new_lesson.ROOT / "ШАБЛОН_КОНСПЕКТА.md").read_text(encoding="utf-8")
        with tempfile.TemporaryDirectory() as temp, patch.object(new_lesson, "ROOT", Path(temp)):
            (Path(temp) / "ШАБЛОН_КОНСПЕКТА.md").write_text(template, encoding="utf-8")
            lecture = new_lesson.create_lesson("dm", date(2026, 10, 1), "Отношения", "лекция")
            lecture.write_text("# Отношения\n\nМатериал лекции.\n", encoding="utf-8")
            lecture_index = (lecture.parent / "README.md").read_text(encoding="utf-8")
            practice = new_lesson.create_lesson("dm", date(2026, 10, 1), "Отношения", "практика")
            self.assertEqual(practice.parent.name, "практики")
            self.assertNotEqual(practice, lecture)
            self.assertEqual(lecture.read_text(encoding="utf-8"), "# Отношения\n\nМатериал лекции.\n")
            self.assertEqual((lecture.parent / "README.md").read_text(encoding="utf-8"), lecture_index)
            practice_index = (practice.parent / "README.md").read_text(encoding="utf-8")
            link = re.search(r"\[Открыть\]\(([^)]+)\)", practice_index)
            self.assertIsNotNone(link)
            self.assertEqual(practice.parent / unquote(link.group(1)), practice)

    def test_rejects_invalid_windows_filename(self) -> None:
        with self.assertRaises(ValueError):
            new_lesson.safe_topic("Введение: множества")


if __name__ == "__main__":
    unittest.main()
