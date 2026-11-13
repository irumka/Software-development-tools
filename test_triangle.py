import unittest
from triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):

    def test_area_zero_height(self):
        res = area(6, 0)
        self.assertEqual(res, 0.0)

    def test_area_zero_base(self):
        res = area(0, 5)
        self.assertEqual(res, 0.0)

    def test_area_six_by_four(self):
        res = area(6, 4)
        self.assertEqual(res, 12.0)

    def test_area_unit_triangle(self):
        res = area(1, 1)
        self.assertEqual(res, 0.5)

    def test_area_ten_by_ten(self):
        res = area(10, 10)
        self.assertEqual(res, 50.0)

    def test_perimeter_zero_sides(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_perimeter_three_four_five(self):
        res = perimeter(3, 4, 5)
        self.assertEqual(res, 12)

    def test_perimeter_equilateral_triangle(self):
        res = perimeter(2, 2, 2)
        self.assertEqual(res, 6)

    def test_perimeter_isosceles_triangle(self):
        res = perimeter(5, 5, 8)
        self.assertEqual(res, 18)

    def test_perimeter_unit_sides(self):
        res = perimeter(1, 1, 1)
        self.assertEqual(res, 3)