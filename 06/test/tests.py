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
        coordinates_list = ["0, 0","3, 0", "0, 3", "3, 3", "2, 2"]
        self.test_grid = Grid(coordinates_list)
        self.test_coordinate = Coordinate("1, 2")
        self.test_coordinate_2 = Coordinate("2, 3")
    
    def test_init(self):
        self.assertEqual(self.test_grid.height, 4)
        self.assertEqual(self.test_grid.width, 4)

    def test_create(self):
        self.assertEqual(self.test_grid.grid, [["", "", "", ""],
                                                    ["", "", "", ""],
                                                    ["", "", "", ""],
                                                    ["", "", "", ""]])
    
    def test_populate(self):
        self.test_grid.populate()
        self.assertEqual(self.test_grid.grid, [["44", "", "", "46"],
                                                    ["", "", "", ""],
                                                    ["", "", "48", ""],
                                                    ["45", "", "", "47"]])
    
    def test_add(self):
        self.test_grid.add(self.test_coordinate)
        self.assertEqual(self.test_grid.grid, [["", "", "", ""],
                                                ["", "", "7", ""],
                                                ["", "", "", ""],
                                                ["", "", "", ""]])
    
    def test_get_manhattan_distance(self):
        self.test_grid.add(self.test_coordinate)
        self.test_grid.add(self.test_coordinate_2)
        self.assertEqual(self.test_grid.get_manhattan_distance(self.test_coordinate, self.test_coordinate_2), 2)

    def test_find_nearest_point(self):
        self.test_grid.add(self.test_coordinate)
        self.test_grid.add(self.test_coordinate_2)
        self.assertEqual(self.test_grid.find_nearest_point(self.test_coordinate), 27)

    def test_add_nearest_points(self):
        self.test_grid.populate()
        self.test_grid.add_nearest_points()
        self.assertEqual(self.test_grid.grid, [["12",12,14,"14"],
                                    [12,0,16,14],
                                    [13, 16, "16", 0],
                                    ["13", 13, 0, "15"]])


if __name__ == "__main__":
    unittest.main()