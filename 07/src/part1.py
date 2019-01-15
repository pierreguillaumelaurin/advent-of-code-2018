import sys
sys.path.insert(0, '../../util/')
import utils

with open("../input/test_input.txt", "r") as input:
    data = input.readlines()
    lines = [line.split(" ") for line in data]

available = []
executed = []

def find_root():
    contingent_steps = []
    for line in lines:
            if line[7] not in available:
                contingent_steps.append(line[7])
    for line in lines:
            if line[1] not in available:
                return line[1]

def find_available_steps():
    for line in lines:
            if line[1] not in available:
                available.append(line[7])
    for line in lines:
        if line[7] in available and line[1] not in executed:
            available.remove(line[7])

def execute_step():
    available.sort()
    step_to_execute = available[0]
    available.remove(step_to_execute)
    executed.append(step_to_execute)


if __name__ == "__main__":
    #assert(lines[0] == ["Step", "I", "must", "be", "finished", "before" ,"step" ,"G" ,"can" , "begin.\n"])
    assert(find_root() == "C")
    available.append(find_root())
    while True:
        find_available_steps()
        execute_step()
        if len(executed) == 6:
            break
    print("".join(executed))

