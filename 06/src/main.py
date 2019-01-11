import re
import sys
sys.path.insert(0, '../../util/')
import utils

with open("../input/input.txt", "r") as input:
    data = input.read()

class Coordinate():
    def __init__(self, str_version):
        self.str_version = str_version
        self.x = utils.get_digits_group(self.str_version, 0)
        self.y = utils.get_digits_group(self.str_version, 1)
        

class Grid():
    def __init__(self, coordinates_list):
        self.coordinates = [Coordinate(line) for line in coordinates_list]
        self.height = self.find_format()[0]
        self.width = self.find_format()[1]
        
    def find_format(self):
        height = max([coordinate.x for coordinate in self.coordinates])
        width = max([coordinate.y for coordinate in self.coordinates])
        return (height, width)