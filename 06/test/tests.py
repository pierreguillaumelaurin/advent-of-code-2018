import unittest
import sys
sys.path.insert(0, '../src/')

from main import Coordinate, Grid

class CoordinateTestCase(unittest.TestCase):
    def setUp(self):
        self.coordinate = Coordinate("287, 68")
    
    def test_init(self):
        self.assertEqual(self.coordinate.x, 287)
        self.assertEqual(self.coordinate.y, 68)
        self.assertEqual(self.coordinate.id, 1)


class GridTestCase(unittest.TestCase):
    def setUp(self):
        coordinates_list = ["0, 0","1, 1", "1, 0", "0, 2"]
        self.test_grid = Grid(coordinates_list)
    
    def test_init(self):
        self.assertEqual(self.test_grid.height, 2)
        self.assertEqual(self.test_grid.width, 3)

    def test_create(self):
        self.assertEqual(self.test_grid.grid, [["", "", ""],
                                                    ["", "", ""]])
    
    def test_populate(self):
        self.test_grid.populate()
        self.assertEqual(self.test_grid.grid, [["10", "", "13"],
                                                   ["12", "11", ""]])


if __name__ == "__main__":
    unittest.main()