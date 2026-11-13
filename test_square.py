import unittest
from square import area, perimeter


class SquareTestCase(unittest.TestCase):

    def test_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_unit_side(self):
        res = area(1)
        self.assertEqual(res, 1)

    def test_area_side_two(self):
        res = area(2)
        self.assertEqual(res, 4)

    def test_area_side_five(self):
        res = area(5)
        self.assertEqual(res, 25)

    def test_area_side_ten(self):
        res = area(10)
        self.assertEqual(res, 100)

    def test_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_unit_side(self):
        res = perimeter(1)
        self.assertEqual(res, 4)

    def test_perimeter_side_two(self):
        res = perimeter(2)
        self.assertEqual(res, 8)

    def test_perimeter_side_five(self):
        res = perimeter(5)
        self.assertEqual(res, 20)

    def test_perimeter_side_ten(self):
        res = perimeter(10)
        self.assertEqual(res, 40)