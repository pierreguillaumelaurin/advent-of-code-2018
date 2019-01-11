with open("../input/input.txt", "r") as input:
    data = input.read()

class Polymer():
    def __init__(self, data):
        self.units = list(data)
        self.react()
        self.final_length = len(self.units)

    def react(self):
        i = 0
        while i < len(self.units) - 1:
            if self.match(self.units[i], self.units[i+1]):
                del self.units[i:i+2]
                i = max(i - 1, 0)
            else:
                i += 1

    def solve_part_1(self):
        return "The answer for part 1 is " + str(self.final_length) + "."
    
    def solve_part_2(self):
        min_units = self.final_length
        charcode = 65
        while charcode < 91:
            test_without_char = list(filter(lambda a: a != chr(charcode) and a != chr(charcode+32), self.units))
            test_polymer = Polymer(test_without_char)
            if test_polymer.final_length < min_units:
                min_units = test_polymer.final_length
            charcode += 1
        return "The answer for part 2 is " + str(min_units) + "."

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
    print(b.solve_part_2())