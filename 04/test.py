import unittest
from part1 import Timetable

test_data = ("[1518-06-12 00:00] Guard #2633 begins shift\n"
            "[1518-06-12 00:09] falls asleep\n"
            "[1518-06-12 00:12] wakes up\n"
            "[1518-07-28 00:00] Guard #2423 begins shift\n"
            "[1518-07-28 00:02] falls asleep\n"
            "[1518-07-28 00:06] wakes up")

data = test_data.split('\n')
data.sort()
test_timetable = Timetable(data)
test_timetable.populate()
if __name__ == "__main__":
    #init tests
    assert(len(test_timetable.matrix) == 3)
    for row in test_timetable.matrix:
        assert(len(row) == 62)

    #split_by_day tests
    assert(len(list(test_timetable.split_by_day(data))) == 2)
    #populate tests
    print(test_timetable.matrix)
    assert(test_timetable.matrix[1][10] == "#")