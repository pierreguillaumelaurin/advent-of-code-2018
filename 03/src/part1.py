import re

with open("../input/input.txt", "r") as input:
    data = input.readlines()

class Claim():
    def __init__(self, claim):
        self.claim = claim
        self.width_offset = self.get_digits_group(claim, 0)
        self.height_offset = self.get_digits_group(claim, 1)
        self.width = self.get_digits_group(claim, 2)
        self.height = self.get_digits_group(claim, 3)
    
    @staticmethod
    def get_digits_group(line, i):
        matches = re.findall(r'\d\d+', line)
        digits = int(matches[i])
        return digits

class Fabric():
    def __init__(self, length, data):
        self.length = length
        self.data = data
        self.fabric = self.build_fabric()

    def build_fabric(self):
        fabric = []
        for i in range(0,self.length):
            row = []
            for y in range(0,self.length):
                row.append(0)
            fabric.append(row)
        return fabric
    

if __name__ == "__main__":
    a = Fabric(10, data)
    b = Claim("#1 @ 146,196: 19x14")
    assert(len(a.fabric) == 10)
    assert(len(a.fabric[0]) == 10)
    assert(b.width_offset == 146)
    assert(b.height_offset == 196)
    assert(b.width == 19)
    assert(b.height == 14)

