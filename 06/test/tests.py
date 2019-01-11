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


class GridTestCase(unittest.TestCase):
    def setUp(self):
        coordinates_list = ["1, 1","2, 2", "2, 1", "1, 3"]
        self.test_grid = Grid(coordinates_list)
    
    def test_init(self):
        self.assertEqual(self.test_grid.width, 2)
        self.assertEqual(self.test_grid.height, 3)
        self.assertEqual(self.test_grid.grid, [["A", "", "D"],
                                                   ["C", "B", ""],
                                                   ["", "", ""]])


if __name__ == "__main__":
    unittest.main()