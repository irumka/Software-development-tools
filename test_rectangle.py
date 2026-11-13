import unittest
from rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):

    def test_area_zero_height(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_area_unit_rectangle(self):
        res = area(1, 1)
        self.assertEqual(res, 1)

    def test_area_three_by_four(self):
        res = area(3, 4)
        self.assertEqual(res, 12)

    def test_area_square(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_area_large_rectangle(self):
        res = area(1000, 2)
        self.assertEqual(res, 2000)

    def test_perimeter_zero_height(self):
        res = perimeter(10, 0)
        self.assertEqual(res, 20)

    def test_perimeter_unit_rectangle(self):
        res = perimeter(1, 1)
        self.assertEqual(res, 4)

    def test_perimeter_three_by_four(self):
        res = perimeter(3, 4)
        self.assertEqual(res, 14)

    def test_perimeter_square(self):
        res = perimeter(10, 10)
        self.assertEqual(res, 40)

    def test_perimeter_large_rectangle(self):
        res = perimeter(1000, 2)
        self.assertEqual(res, 2004)