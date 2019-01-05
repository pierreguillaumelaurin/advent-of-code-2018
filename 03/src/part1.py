import re

with open("../input/input.txt", "r") as input:
    data = input.readlines()

class Claim_manager():
    def __init__(self, data):
        self.data = data
        self.claims = [Claim(line) for line in data]
        self.overlaps = self.find_overlaps()
    
    def find_overlaps(self):
        for i, claim in enumerate(self.claims):
            y = len(self.claims) - i
            while (y != 0):
                if(self.are_overlapping(self.claims[i], self.claims[y])):
                    overlaps += 1
                y -= 1

    @staticmethod
    def are_overlapping(first_claim, second_claim):
        overlap = False
        if (self.side_overlapping(first_claim,second_claim)
           or self.side_overlapping(second_claim, first_claim)):
            overlap = True
        elif (self.corner_overlapping(first_claim, second_claim)
           or self.corner_overlapping(second_claim, first_claim)):
            overlap = True
        return overlap
    
    @staticmethod
    def side_overlapping(first_claim, second_claim):
        overlap = False
        if ((first_claim.left_width_offset + first_claim.width >= second_claim.left_width_offset + second_claim.width)
            and (first_claim.left_width_offset < second_claim.left_width_offset)):
            overlap = True
        elif (first_claim.left_heigh_offset + first_claim.heigh >= second_claim.left_heigh_offset + second_claim.heigh
            and first_claim.left_heigh_offset < second_claim.left_heigh_offset):
            overlap = True
        return overlap
    
    @staticmethod
    def corner_overlapping(first_claim, second_claim):
        overlap = False
        for corner in second_claim.corners:
            if (first_claim.upper_left_corner < corner
                and first_claim.upper_right_corner > corner
                and first_claim.lower_left_corner < corner
                and first_claim.lower_right_corner > corner):
                overlap = True
        return overlap

        
        



class Claim():
    def __init__(self, claim):
        self.claim = claim
        self.id = self.get_id()
        self.left_width_offset = self.get_left_width_offset()
        self.top_height_offset = self.get_top_height_offset()
        self.width = self.get_width()
        self.height = self.get_height()
        self.upper_left_corner = self.get_upper_left_corner()
        self.upper_right_corner = self.get_upper_right_corner()
        self.lower_right_corner = self.get_lower_right_corner()
        self.lower_left_corner = self.get_lower_left_corner()
        self.corners = self.get_corners()
        
    
    def get_id(self):
        match = re.search('#(.*) @', self.claim)
        return int(match.group(1))
    
    def get_left_width_offset(self):
        match = re.search('@ (.*),', self.claim)
        return int(match.group(1))
    
    def get_top_height_offset(self):
        match = re.search(',(.*):', self.claim)
        return int(match.group(1))
    
    def get_width(self):
        match = re.search(': (.*)x', self.claim)
        return int(match.group(1))
    
    def get_height(self):
        match = re.search('x(.*)$', self.claim)
        return int(match.group(1))

    def get_upper_left_corner(self):
        return (self.left_width_offset, self.top_height_offset)

    def get_upper_right_corner(self):
        return (self.left_width_offset+self.width, self.top_height_offset)
    
    def get_lower_right_corner(self):
        return (self.left_width_offset + self.width,
                self.top_height_offset + self.height)

    def get_lower_left_corner(self):
        return (self.left_width_offset, self.top_height_offset + self.height)
    
    def get_corners(self):
        corners = []
        corners.append(self.get_lower_left_corner)
        corners.append(self.get_lower_right_corner)
        corners.append(self.get_upper_left_corner)
        corners.append(self.get_upper_right_corner)
        return corners
    
if __name__ == "__main__":
    test_data = data[0]
    test_claim = Claim(test_data)

    assert(test_claim.id == 1)
    assert(test_claim.left_width_offset == 146)
    assert(test_claim.top_height_offset == 196)
    assert(test_claim.width == 19)
    assert(test_claim.height == 14)
    assert(test_claim.upper_left_corner == (146, 196))
    assert(test_claim.lower_right_corner == (165, 210))
    assert(test_claim.upper_right_corner == (165, 196))
    assert(test_claim.lower_left_corner == (146, 210))

    claim_manager = Claim_manager(data)
    print(claim_manager.overlaps)
