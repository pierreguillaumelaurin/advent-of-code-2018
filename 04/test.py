import unittest
from part1 import Timetable

class TimetableTestCase(unittest.TestCase):
    def setUp(self):
        data = """[1518-06-12 23:57] Guard #2633 begins shift
               """
        self.test_timetable = Timetable(data)

    def test_init(self):
        self.assertEqual(len(self.test_timetable) == 3)
        for row in self.test_timetable:
            self.assertEqual(len(row) == 62)

if __name__ == "__main__":
    unittest.main()