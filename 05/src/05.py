import re

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
                    reaction_on_l = ord(self.units[l]) == ord(self.units[l+1]) + 32 or ord(self.units[l]) == ord(self.units[l+1]) - 32
                    iterator = len(self.units) - 2
            if had_reaction and l != 0:
                l -= 1
            else:
                l += 1
    
    def get_units_count(self):
        return len(self.units)

    def solve_part_1(self):
        self.react()
        return "The answer for part 1 is " + str(self.get_units_count()) + "."
    
def test(s, answer=""):
        p = Polymer(s)
        past = p.units
        p.react()
        if answer == "":
            assert(p.units == past)
        else:
            assert(p.units == answer)

if __name__ == "__main__":
    test("dabAcCaCBAcCcaDA", "dabCBAcaDA")
    test("dabAcCaCBAcCcaDABBxx", "dabCBAcaDABBxx")
    test("ACacACacACacACacACacACacACacACacACac")
    test("cAaaC", "caC")


    b = Polymer(data)
    d = b.units
    beginning = b.units
    print(b.solve_part_1())
    assert(d != b.units)
    print(b.units)
    