with open("../input/input.txt", "r") as input:
    data = input.readlines()

double_occurences = 0
triple_occurences = 0

def count_multiple_occurences(id):
    global double_occurences
    global triple_occurences
    letter_appearing_twice = False
    letter_appearing_three_times = False
    for l in set(id):
        if id.count(l) == 2:
            letter_appearing_twice = True
        elif id.count(l) == 3:
            letter_appearing_three_times = True
    if letter_appearing_twice:
        double_occurences += 1
    if letter_appearing_three_times:
        triple_occurences += 1

for id in data:
    if len(id) != len(set(id)):
        count_multiple_occurences(id)

answer = double_occurences * triple_occurences
print(answer) 

