import unittest
from square import area, perimeter

class SquareTestCase(unittest.TestCase):

    def test_area_1(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_2(self):
        res = area(1)
        self.assertEqual(res, 1)

    def test_area_3(self):
        res = area(2)
        self.assertEqual(res, 4)

    def test_area_4(self):
        res = area(5)
        self.assertEqual(res, 25)

    def test_area_5(self):
        res = area(10)
        self.assertEqual(res, 100)

    def test_perimeter_1(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_2(self):
        res = perimeter(1)
        self.assertEqual(res, 4)

    def test_perimeter_3(self):
        res = perimeter(2)
        self.assertEqual(res, 8)

    def test_perimeter_4(self):
        res = perimeter(5)
        self.assertEqual(res, 20)

    def test_perimeter_5(self):
        res = perimeter(10)
        self.assertEqual(res, 40)