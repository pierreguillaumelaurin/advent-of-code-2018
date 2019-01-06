import sys
import re
import datetime

sys.path.insert(0, '../util')
from utils import multiline_input

data = multiline_input()

schedule = data.split('\n')
schedule.sort()
sleep_log = {}

def split_by_day(schedule):
    day_log = []
    for line in schedule:
        if "#" in line:
            if day_log:
                yield day_log
            day_log = [line]
        else:
            day_log.append(line)
        
daily_schedule = list(split_by_day(schedule))

def initialize_sleep_log(data, sleep_log):
    for event in data:
        if ("#" in event):
            key = get_id(event)
            sleep_log[key] = 0

def get_id(line):
    match = re.search(r'#(\d+) ', line)
    guard_id = match.group(1)
    return guard_id

def get_times_falling_asleep(day):
    times_falling_asleep = []
    for event in day:
        if "falls asleep" in event:
            match = re.search(r' (\d+:\d+)]', event)
            time = match.group(1)
            times_falling_asleep.append(time)
    return times_falling_asleep

def get_times_waking_up(day):
    times_waking_up = []
    for event in day:
        if "wakes up" in event:
            match = re.search(r' (\d+:\d+)]', event)
            time = match.group(1)
            times_waking_up.append(time)
    return times_waking_up

def get_minutes_slept(day):
    minutes_slept = 0
    times_falling_asleep = get_times_falling_asleep(day)
    times_waking_up = get_times_waking_up(day)
    date_format = '%H:%M'
    for time_falling_asleep, time_waking_up in zip(times_falling_asleep, times_waking_up):
        time_difference = datetime.datetime.strptime(time_waking_up, date_format) - datetime.datetime.strptime(time_falling_asleep, date_format)
        difference_in_minutes = int(time_difference.total_seconds()/60)
        minutes_slept += difference_in_minutes
    return minutes_slept

initialize_sleep_log(schedule, sleep_log)

for day in daily_schedule:
    line_with_id = day[0]
    guard_id = get_id(line_with_id)
    a = get_minutes_slept(day)
    sleep_log[guard_id] += get_minutes_slept(day)
print(sleep_log)

"""
i = 0
key = ""
format = '%H:%M'

while i != len(schedule):
    if ("#" in schedule[i]):
        match = re.search(r'#(\d+) ')
        key = match.group(1)
    elif ("falls asleep" in schedule[i]):
        match = re.search(r' (\d+)]')
        minutes_slept[key] += int(match)
    i += 1
"""