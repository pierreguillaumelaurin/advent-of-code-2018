import re
import string

with open("../input/input.txt", "r") as input:
    data = input.read()

class Polymer():
    def __init__(self, data):
        self.units = data

    def react(self):
        iterator = len(self.units) - 2
        has_reaction = False
        reactions = []
        for l in range(0,iterator):
            reaction_on_l = self.units[l] == self.units[l+1].upper() or self.units[l] == self.units[l+1].lower()
            if (reaction_on_l):
                units_involved = self.units[l] + self.units[l+1]
                has_reaction = True
                reactions.append(units_involved)
        if has_reaction:
            self.remove_reactions(reactions)
            self.react()

    def remove_reactions(self, reactions):
        for reaction in reactions:
            self.units = self.units.replace(reaction, "")

    def get_units_count(self):
        return len(self.units)

    def solve_part_1(self):
        self.react()
        return "The answer for part 1 is " + str(self.get_units_count()) + "."
    

if __name__ == "__main__":
    a = Polymer("dabAcCaCBAcCcaDA")
    assert(a.get_units_count() == 16)
    a.react()
    assert(a.units == "dabCBAcaDA")
    assert(a.get_units_count() == 10)
    b = Polymer(data)
    beginning = b.units
    print(b.solve_part_1())
    print(b.units)