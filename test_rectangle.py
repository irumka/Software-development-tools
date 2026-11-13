import unittest
from rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):

    def test_area_zero_height(self):
        self.assertEqual(area(10, 0), 0)

    def test_area_unit_rectangle(self):
        self.assertEqual(area(1, 1), 1)

    def test_area_three_by_four(self):
        self.assertEqual(area(3, 4), 12)

    def test_area_square(self):
        self.assertEqual(area(10, 10), 100)

    def test_area_large_rectangle(self):
        self.assertEqual(area(1000, 2), 2000)

    def test_area_negative_width(self):
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

    def test_perimeter_zero_height(self):
        self.assertEqual(perimeter(10, 0), 20)

    def test_perimeter_unit_rectangle(self):
        self.assertEqual(perimeter(1, 1), 4)

    def test_perimeter_three_by_four(self):
        self.assertEqual(perimeter(3, 4), 14)

    def test_perimeter_square(self):
        self.assertEqual(perimeter(10, 10), 40)

    def test_perimeter_large_rectangle(self):
        self.assertEqual(perimeter(1000, 2), 2004)

    def test_perimeter_negative_width(self):
        with self.assertRaises(ValueError):
            perimeter(-5, 2)

    def test_perimeter_negative_height(self):
        with self.assertRaises(ValueError):
            perimeter(5, -2)

    def test_perimeter_string(self):
        with self.assertRaises(TypeError):
            perimeter("5", 2)

    def test_perimeter_none(self):
        with self.assertRaises(TypeError):
            perimeter(5, None)
