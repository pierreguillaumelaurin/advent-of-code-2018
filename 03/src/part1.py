import re

with open("../input/input.txt", "r") as input:
    data = input.readlines()

class Claim():
    def __init__(self, claim):
        self.claim = claim
        self.width_offset = self.get_digits_group(claim, 1)
        self.height_offset = self.get_digits_group(claim, 2)
        self.width = self.get_digits_group(claim, 3)
        self.height = self.get_digits_group(claim, 4)
    
    @staticmethod
    def get_digits_group(line, i):
        matches = re.findall(r'\d+', line)
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
    
    def add_claims(self):
        claims = (Claim(row) for row in self.data)
        for claim in claims:
            self.fill_rectangle(claim)

    def fill_rectangle(self, claim):
        i = claim.height_offset
        y = claim.width_offset
        i_counter = claim.height
        y_counter = claim.width
        while i_counter != 0:
            while y_counter != 0:
                try:
                    self.fabric[i+i_counter-1][y+y_counter-1] += 1
                except (IndexError):
                    print("claim ",claim.claim, " requests a square inch out of the fabric (position:",i+i_counter-1, y+y_counter,")." )
                    raise IndexError
                y_counter -= 1
            i_counter -= 1
            y_counter = claim.width

    def solve_part_1(self):
        counter = 0
        for row in self.fabric:
            for sqr_inch in row:
                if (sqr_inch > 1):
                    counter += 1
        return counter
            
            


    

if __name__ == "__main__":
    a = Fabric(1000, data)
    b = Claim("#1 @ 146,196: 19x14")
    assert(len(a.fabric) == 1000)
    assert(len(a.fabric[0]) == 1000)
    """
    for row in a.fabric:
        for sqr_inch in row:
            assert(sqr_inch == 0)
    """
    assert(b.width_offset == 146)
    assert(b.height_offset == 196)
    assert(b.width == 19)
    assert(b.height == 14)
    a.add_claims()
    print(a.fabric)
    print(a.solve_part_1())

