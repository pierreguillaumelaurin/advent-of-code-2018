import sys
import re
import datetime

sys.path.insert(0, '../util')
from utils import multiline_input

def initialize_sleep_log(data, sleep_log):
    for event in data:
        if ("#" in event):
            key = get_id(event)
            sleep_log[key] = 0

def get_times_falling_asleep(day):
    times_falling_asleep = []
    date_format = '%H:%M'
    for event in day:
        if "falls asleep" in event:
            match = re.search(r' (\d+:\d+)]', event)
            time = match.group(1)
            time = datetime.datetime.strptime(time, date_format)
            times_falling_asleep.append(time)
    return times_falling_asleep

def get_times_waking_up(day):
    times_waking_up = []
    date_format = '%H:%M'
    for event in day:
        if "wakes up" in event:
            match = re.search(r' (\d+:\d+)]', event)
            time = match.group(1)
            time = datetime.datetime.strptime(time, date_format)
            times_waking_up.append(time)
    return times_waking_up

def fill_log(daily_schedule, sleep_log):
    for day in daily_schedule:
        line_with_id = day[0]
        guard_id = get_id(line_with_id)
        a = get_minutes_slept(day)
        sleep_log[guard_id] += get_minutes_slept(day)
    return sleep_log

def find_biggest_sleeper(sleep_log):
    return max(sleep_log, key= sleep_log.get)

class Timetable():
    def __init__(self, data):
        self.data = data
        self.matrix = []
        first_row = []
        for i in range(-2,60):
            first_row.append(i)
        self.matrix.append(first_row)
        for line in self.data:
            if "#" in line:
                row = []
                date = self.get_date(line)
                row.append(date)
                guard_id = self.get_id(line)
                row.append(guard_id)
                for column in range(0, 60):
                    row.append(".")
                self.matrix.append(row)
        self.populate()
        self.minutes_slept = self.get_minutes_slept()
    
    def populate(self):
        daytables = list(self.split_by_day(self.data))
        for i in range(0, len(self.matrix)-2):
            marker = "."
            for y in range(2,62):
                time = y-2
                minute_log = ":{0:0=2d}".format(time)
                events = [event for event in daytables[i]]
                if [event for event in events if minute_log in event]:
                    if [event for event in events if minute_log + "] falls asleep" in event]:
                        marker = "#"
                    elif [event for event in events if minute_log + "] wakes up" in events]:
                        marker = "."
                self.matrix[i+2][y] = marker
    
    def get_minutes_slept(self):
        minutes_slept = {}
        for row in self.matrix:
            guard_id = row[1]
            minutes_slept[guard_id] = 0
        for row in self.matrix:
            guard_id = row[1]
            minutes_slept[guard_id] += row.count("#")
        return minutes_slept

    def solve_part_1(self):
        biggest_sleeper = self.get_biggest_sleeper()
        minute_slept_the_most = self.get_minute_spent_asleep_the_most(biggest_sleeper)
        return int(biggest_sleeper) * minute_slept_the_most
    
    def get_biggest_sleeper(self):
        return max(self.minutes_slept, key= self.minutes_slept.get)

    def get_minute_spent_asleep_the_most(self, guard_id):
        minutes_slept = {}
        for minute in range(0, 60):
            minutes_slept[minute] = 0
        for row in self.matrix:
            if row[1] == guard_id:
                for i in range(2, 62):
                    if row[i] == "#":
                        minutes_slept[i-2] += 1
        return max(minutes_slept, key=minutes_slept.get)
                    
    def __repr__(self):
        return str(self.matrix)

    @staticmethod
    def get_id(line):
        match = re.search(r'#(\d+) ', line)
        guard_id = match.group(1)
        return guard_id

    @staticmethod
    def get_date(line):
        match_date = re.search(r'-\d\d-\d\d', line)
        date = match_date.group(0)
        return date
    
    @staticmethod
    def split_by_day(schedule):
        day_log = []
        for line in schedule:
            if "#" in line:
                if day_log:
                    yield day_log
                day_log = [line]
            else:
                day_log.append(line)

if __name__ == "__main__":
    data = multiline_input()
    data = data.split('\n')
    data.sort()
    a = Timetable(data)
    a.get_minute_spent_asleep_the_most("2393")
    print(a.solve_part_1())
