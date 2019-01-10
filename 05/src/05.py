import re
import string

with open("../input/input.txt", "r") as input:
    data = input.read()

class Polymer():
    def __init__(self, data):
        self.units = data

    def react(self):
        l = 0
        iterator = len(self.units) - 2
        while l != iterator:
            reaction_on_l = ord(self.units[l]) == ord(self.units[l+1]) + 32 or ord(self.units[l]) == ord(self.units[l+1]) - 32
            had_reaction = False
            while reaction_on_l:
                    had_reaction = True
                    units_involved = self.units[l] + self.units[l+1]
                    past = self.units
                    self.units = self.units.replace(units_involved, "", 1)
                    print(units_involved)
                    reaction_on_l = ord(self.units[l]) == ord(self.units[l+1]) + 32 or ord(self.units[l]) == ord(self.units[l+1]) - 32
                    iterator = len(self.units) - 2
            if had_reaction:
                l -= 1
            else:
                l += 1

    def get_units_count(self):
        return len(self.units)

    def solve_part_1(self):
        self.react()
        return "The answer for part 1 is " + str(self.get_units_count()) + "."
    

if __name__ == "__main__":
    a = Polymer("dabAcCaCBAcCcaDA")
    assert(a.get_units_count() == 16)
    a.react()
    print(a.units)
    assert(a.units == "dabCBAcaDA")
    assert(a.get_units_count() == 10)
    c = Polymer("dabAcCaCBAcCcaDABBxx")
    c.react()
    assert(c.units == "dabCBAcaDABBxx")
    b = Polymer(data)
    d = b.units
    beginning = b.units
    print(b.solve_part_1())
    assert(d != b.units)
    print(b.units)