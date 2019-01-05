import sys
import re
import datetime

sys.path.insert(0, '../util')
from utils import multiline_input

data = multiline_input()

schedule = data.split('\n')
schedule.sort()
minutes_slept = {}

def split_by_day(schedule):
    day_log = []
    for line in schedule:
        if "#" in line:
            yield day_log
            day_log = [line]
        else:
            day_log.append(line)
        
daily_schedule = list(split_by_day(schedule))

def initialize_sleep_log(data, sleep_log):
    for event in data:
        if ("#" in event):
            match = re.search(r'#(\d+) ', event)
            key = match.group(1)
            sleep_log[key] = 0

initialize_sleep_log(schedule, minutes_slept)
print(minutes_slept)
for day in daily_schedule:
    print(day)

i = 0
key = ""
format = '%H:%M'
"""
while i != len(schedule):
    if ("#" in schedule[i]):
        match = re.search(r'#(\d+) ')
        key = match.group(1)
    elif ("falls asleep" in schedule[i]):
        match = re.search(r' (\d+)]')
        minutes_slept[key] += int(match)
    i += 1
"""