import re
import sys
sys.path.insert(0, '../../util/')
import utils
import itertools

with open("../input/input.txt", "r") as input:
    data = input.read()

coordinates_list = ["0, 0","3, 0", "0, 3", "3, 3", "2, 2"]

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
    
    def add(self, coordinate):
        self.grid[coordinate.x][coordinate.y] = str(coordinate.id)

    def find_nearest_point(self, coordinate):
        biggest_distance = self.height + self.width
        nearest_point = 0
        for second_coordinate in self.coordinates:
            distance = self.get_manhattan_distance(coordinate, second_coordinate)
            if distance < biggest_distance:
                biggest_distance = distance
                nearest_point = second_coordinate.id
            elif distance == biggest_distance:
                nearest_point = 0
        return nearest_point

    def get_manhattan_distance(self, coordinate_1, coordinate_2):
        return abs(coordinate_2.x - coordinate_1.x) + abs(coordinate_2.y - coordinate_1.y)

    def add_nearest_points(self):
        for row in range(0, self.height):
            for column in range(0, self.width):
                coordinate = Coordinate(str(row)+ ", "+ str(column))
                self.grid[row-1][column-1] = self.find_nearest_point(coordinate)


if __name__ == "__main__":
    a = Grid(coordinates_list)
    a.populate()
    print(a.grid)