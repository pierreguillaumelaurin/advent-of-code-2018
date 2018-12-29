with open("../input/input.txt", "r") as input:
    data = input.readlines()

class Id_checker():
    def __init__(self, data):
        self.data = data
        self.double_occurences = 0
        self.triple_occurences = 0
        self.answer = self.double_occurences * self.triple_occurences

    def count_multiple_occurences(self, id):
        letter_appearing_twice = False
        letter_appearing_three_times = False
        for l in set(id):
            if id.count(l) == 2:
                letter_appearing_twice = True
            elif id.count(l) == 3:
                letter_appearing_three_times = True
        if letter_appearing_twice:
            self.double_occurences += 1
        if letter_appearing_three_times:
            self.triple_occurences += 1

    def checksum(self):
        for id in self.data:
            if len(id) != len(set(id)):
                self.count_multiple_occurences(id)

    def answer_part_one(self):
        self.checksum()
        print(self.double_occurences * self.triple_occurences)

id_checker = Id_checker(data)
id_checker.answer_part_one()