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