from collections import Counter

with open("../input/input.txt", "r") as input:
    data = input.readlines()

class Prototype_Finder():
    def __init__(self, data):
        self.data = data
    
    def find_prototypes(self):
        separator = 1
        while separator != len(self.data)-1:
            substrings = (id[:separator]+ id[separator+1:] for id in data)
            counts = Counter(substrings)
            if 2 in counts.values():
                answer = list(counts.keys())[list(counts.values()).index(2)]
                return (answer)
            separator += 1

if __name__ == "__main__":
    prototype_finder = Prototype_Finder(data)
    print(prototype_finder.find_prototypes())