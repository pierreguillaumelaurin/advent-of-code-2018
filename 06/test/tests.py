import unittest
import sys
sys.path.insert(0, '../src/')

from main import Coordinate

class CoordinateTestCase(unittest.TestCase):
    def setUp(self):
        self.coordinate = Coordinate("287, 68")
    
    def test_init(self):
        self.assertEqual(self.coordinate.x, 287)
        self.assertEqual(self.coordinate.y, 68)


if __name__ == "__main__":
    unittest.main()