import unittest
from triangle import area, perimeter

class TriangleTestCase(unittest.TestCase):

    def test_area_zero_height(self):
        self.assertEqual(area(6, 0), 0.0)

    def test_area_zero_base(self):
        self.assertEqual(area(0, 5), 0.0)

    def test_area_six_by_four(self):
        self.assertEqual(area(6, 4), 12.0)

    def test_area_unit_triangle(self):
        self.assertEqual(area(1, 1), 0.5)

    def test_area_ten_by_ten(self):
        self.assertEqual(area(10, 10), 50.0)

    def test_area_negative_base(self):
        with self.assertRaises(ValueError):
            area(-5, 2)

    def test_area_negative_height(self):
        with self.assertRaises(ValueError):
            area(5, -2)

    def test_area_string(self):
        with self.assertRaises(TypeError):
            area("5", 2)

    def test_area_none(self):
        with self.assertRaises(TypeError):
            area(5, None)

    def test_perimeter_zero_sides(self):
        self.assertEqual(perimeter(0, 0, 0), 0)

    def test_perimeter_three_four_five(self):
        self.assertEqual(perimeter(3, 4, 5), 12)

    def test_perimeter_equilateral_triangle(self):
        self.assertEqual(perimeter(2, 2, 2), 6)

    def test_perimeter_isosceles_triangle(self):
        self.assertEqual(perimeter(5, 5, 8), 18)

    def test_perimeter_unit_sides(self):
        self.assertEqual(perimeter(1, 1, 1), 3)

    def test_perimeter_negative_side(self):
        with self.assertRaises(ValueError):
            perimeter(-3, 4, 5)

    def test_perimeter_string(self):
        with self.assertRaises(TypeError):
            perimeter("3", 4, 5)

    def test_perimeter_none(self):
        with self.assertRaises(TypeError):
            perimeter(3, None, 5)
