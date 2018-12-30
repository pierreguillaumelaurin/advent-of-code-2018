import re

with open("../input/input.txt", "r") as input:
    data = input.readlines()

class Claim_manager():
    def __init__(self, data):
        self.data = data
        self.claim_overlaps = 0
    
    #def find_claim_overlaps(self):


class Claim():
    def __init__(self, claim):
        self.claim = claim
        self.id = self.set_id()
        self.left_width_offset = self.set_left_width_offset()
        self.top_height_offset = self.set_top_height_offset()
        self.width = self.set_width()
        self.height = self.set_height()
    
    def set_id(self):
        match = re.search('#(.*) @', self.claim)
        return int(match.group(1))
    
    def set_left_width_offset(self):
        match = re.search('@ (.*),', self.claim)
        return int(match.group(1))
    
    def set_top_height_offset(self):
        match = re.search(',(.*):', self.claim)
        return int(match.group(1))
    
    def set_width(self):
        match = re.search(': (.*)x', self.claim)
        return int(match.group(1))
    
    def set_height(self):
        match = re.search('x(.*)$', self.claim)
        return int(match.group(1))

if __name__ == "__main__":
    test_data = data[0]
    test_claim = Claim(test_data)

    assert(test_claim.id == 1)
    assert(test_claim.left_width_offset == 146)
    assert(test_claim.top_height_offset == 196)
    assert(test_claim.width == 19)
    assert(test_claim.height == 14)