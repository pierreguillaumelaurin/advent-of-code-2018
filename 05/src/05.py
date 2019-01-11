with open("../input/input.txt", "r") as input:
    data = input.read()

class Polymer():
    def __init__(self, data):
        self.units = list(data)

    def react(self):
        i = 0
        while i < len(self.units) - 1:
            if self.match(self.units[i], self.units[i+1]):
                del self.units[i:i+2]
                i = max(i - 1, 0)
            else:
                i += 1

    def get_units_count(self):
        return len(self.units)

    def solve_part_1(self):
        self.react()
        return "The answer for part 1 is " + str(self.get_units_count()) + "."

    @staticmethod
    def match(l, m):
        difference = ord('a') - ord('A')
        return abs(ord(l) - ord(m)) == difference
    
def test(s, answer=""):
        p = Polymer(s)
        p.react()
        if answer == "":
            past = p.units
            assert(p.units == past)
        else:
            try:
                assert(p.units == answer)
            except AssertionError:
                print(p.units)

if __name__ == "__main__":
    test("dabAcCaCBAcCcaDA", "dabCBAcaDA")
    test("dabAcCaCBAcCcaDABBxx", "dabCBAcaDABBxx")
    test("ACacACacACacACacACacACacACacACacACac")
    test("cAaaC", "caC")

    b = Polymer(data)
    print(b.solve_part_1())    