import sys
from part1 import Timetable

sys.path.insert(0, '../util')
from utils import multiline_input

if __name__ == "__main__":
    data = multiline_input()
    data = data.split('\n')
    data.sort()
    a = Timetable(data)
    print(a.solve_part_2())