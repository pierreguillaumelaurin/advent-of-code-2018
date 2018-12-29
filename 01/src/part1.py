answer = 0

with open("../input/input.txt", "r") as input:
    data = input.readlines()

print(sum((int(number) for number in data))) #part 1

