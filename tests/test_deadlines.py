from __future__ import annotations

import tempfile
import unittest
from datetime import date
from pathlib import Path

from tools import deadlines


ACTIVE_TEXT = """# Текущие

<!-- DEADLINES:START -->
| ID | Дисциплина | Дата | Задача | Статус | Источник и уточнение | Пометка |
|---|---|---|---|---|---|---|
| A-1 | Математика | 2026-09-28 | Домашняя работа | TODO | преподаватель, 27.09 | впереди |
| A-2 | Математика | неизвестна | Лабораторная | BLOCKED | преподаватель, 27.09 | уточнить дату |
<!-- DEADLINES:END -->
"""

ARCHIVE_TEXT = """# Архив

<!-- DEADLINES:START -->
| ID | Дисциплина | Дата | Задача | Итог | Источник и уточнение | Перенесено (МСК) | Причина |
|---|---|---|---|---|---|---|---|
<!-- DEADLINES:END -->
"""


class DeadlineSyncTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        base = Path(self.temp.name)
        self.active = base / "ДЕДЛАЙНЫ.md"
        self.archive = base / "АРХИВ.md"
        self.active.write_text(ACTIVE_TEXT, encoding="utf-8")
        self.archive.write_text(ARCHIVE_TEXT, encoding="utf-8")

    def test_overdue_open_task_stays_active(self) -> None:
        moved, changed = deadlines.sync(self.active, self.archive, date(2026, 9, 29))
        self.assertEqual(moved, 0)
        self.assertTrue(changed)
        self.assertIn("| A-1 | Математика | 2026-09-28 | Домашняя работа | TODO | преподаватель, 27.09 | просрочен |", self.active.read_text(encoding="utf-8"))
        self.assertNotIn("A-1", self.archive.read_text(encoding="utf-8"))

    def test_closed_task_moves_once_and_keeps_history(self) -> None:
        self.active.write_text(ACTIVE_TEXT.replace("Домашняя работа | TODO", "Домашняя работа | DONE"), encoding="utf-8")
        moved, changed = deadlines.sync(self.active, self.archive, date(2026, 9, 29))
        self.assertEqual((moved, changed), (1, True))
        self.assertNotIn("A-1", self.active.read_text(encoding="utf-8"))
        self.assertIn("| A-1 | Математика | 2026-09-28 | Домашняя работа | DONE | преподаватель, 27.09 | 2026-09-29 | выполнено |", self.archive.read_text(encoding="utf-8"))
        moved, changed = deadlines.sync(self.active, self.archive, date(2026, 9, 29))
        self.assertEqual((moved, changed), (0, False))

    def test_bad_date_does_not_change_files(self) -> None:
        invalid = ACTIVE_TEXT.replace("2026-09-28", "28.09.2026")
        self.active.write_text(invalid, encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Дата должна"):
            deadlines.sync(self.active, self.archive, date(2026, 9, 29))
        self.assertEqual(self.active.read_text(encoding="utf-8"), invalid)
        self.assertEqual(self.archive.read_text(encoding="utf-8"), ARCHIVE_TEXT)


if __name__ == "__main__":
    unittest.main()
