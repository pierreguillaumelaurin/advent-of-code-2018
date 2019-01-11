import re
import sys
sys.path.insert(0, '../../util/')
import utils

with open("../input/input.txt", "r") as input:
    data = input.read()

class Coordinate():
    new_id = 0
    def __init__(self, str_version):
        self.str_version = str_version
        self.x = utils.get_digits_group(self.str_version, 0)
        self.y = utils.get_digits_group(self.str_version, 1)
        Coordinate.new_id += 1
        self.id = Coordinate.new_id

class Grid():
    def __init__(self, coordinates_list):
        self.coordinates = [Coordinate(line) for line in coordinates_list]
        self.height = self.find_format()[0]
        self.width = self.find_format()[1]
        self.grid = self.create()

    def find_format(self):
        height = max([coordinate.x for coordinate in self.coordinates])+1
        width = max([coordinate.y for coordinate in self.coordinates])+1
        return (height, width)

    def create(self):
        return [["" for y in range(0, self.width)] for x in range(0, self.height)]

    def populate(self):
        for coordinate in self.coordinates:
            self.grid[coordinate.x][coordinate.y] = str(coordinate.id)

