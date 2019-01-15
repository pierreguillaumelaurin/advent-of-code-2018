import sys
sys.path.insert(0, '../../util/')
import utils

with open("../input/input.txt", "r") as input:
    data = input.readlines()
    lines = [line.split(" ") for line in data]

executed = []
pipeline = []
steps_not_executed = {}

for line in lines:
    steps_not_executed[line[7]] = []
    steps_not_executed[line[1]] = []

#assert(steps_not_executed == {"A": [], "B": [], "C": [], "D": [], "E": [], "F": []})

for line in lines:
    steps_not_executed[line[7]].append(line[1])

#assert(steps_not_executed == {"A": ["C"], "B": ["A"], "C": [], "F": ["C"], "D": ["A"], "E": ["B", "D", "F"]})


def add_to_pipeline():
    to_delete = []
    for key, value in steps_not_executed.items():
        if not value:
            pipeline.append(key)
            to_delete.append(key)
    for key in to_delete:
        del steps_not_executed[key]

def execute():
    pipeline.sort()
    executed.append(pipeline[0])
    pipeline.remove(pipeline[0])

def update_precondition():
    for value in steps_not_executed.values():
        if executed[-1] in value:
            value.remove(executed[-1])

if __name__ == "__main__":
    while steps_not_executed:
        add_to_pipeline()
        execute()
        update_precondition()
    print("".join(executed))

