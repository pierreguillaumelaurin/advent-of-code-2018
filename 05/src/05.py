import re
import string

with open("../input/input.txt", "r") as input:
    data = input.read()

with open("../input/test.txt", "r") as input:
    test_data = input.read()

class Polymer():
    def __init__(self, data):
        self.units = data

    def react(self):
        matches = re.findall(r'[A-Z][a-z]|[a-z][A-Z]', self.units)
        if matches:
            for match in matches:
                self.units = self.units.replace(match, "")
            self.react()

    def get_units_count(self):
        return len(self.units)

    def solve_part_1(self):
        self.react()
        return "The answer for part 1 is " + str(self.get_units_count()) + "."

if __name__ == "__main__":
    a = Polymer("dabAcCaCBAcCcaDA")
    assert(a.get_units_count() == 16)
    a.react()
    print("units: ", a.units)
    assert(a.units == "dabCBAcaDA")
    assert(a.get_units_count() == 10)
    c = Polymer(test_data)
    c.react()
    assert(c.units == "ccc")
    assert(c.get_units_count())
    b = Polymer(data)
    print(b.solve_part_1())