from collections import Counter

with open("../input/input.txt", "r") as input:
    data = input.readlines()

class Id_checker():
    def __init__(self, data):
        self.data = data
        self.double_occurences = 0
        self.triple_occurences = 0

    def checksum(self):
        for id in self.data:
            counter = Counter(id)
            if 2 in counter.values():
                self.double_occurences += 1
            if 3 in counter.values():
                self.triple_occurences += 1

    def answer_part_one(self):
        self.checksum()
        return self.double_occurences * self.triple_occurences

if __name__ == "__main__":
    id_checker = Id_checker(data)
    print(id_checker.answer_part_one())