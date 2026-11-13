import unittest
from square import area, perimeter


class SquareTestCase(unittest.TestCase):

    def test_area_zero(self):
        self.assertEqual(area(0), 0)

    def test_area_unit_side(self):
        self.assertEqual(area(1), 1)

    def test_area_side_two(self):
        self.assertEqual(area(2), 4)

    def test_area_side_five(self):
        self.assertEqual(area(5), 25)

    def test_area_side_ten(self):
        self.assertEqual(area(10), 100)

    def test_area_fractional_side(self):
        self.assertEqual(area(0.5), 0.25)

    def test_area_negative_side(self):
        with self.assertRaises(ValueError):
            area(-5)

    def test_area_string(self):
        with self.assertRaises(TypeError):
            area("5")

    def test_area_none(self):
        with self.assertRaises(TypeError):
            area(None)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_unit_side(self):
        self.assertEqual(perimeter(1), 4)

    def test_perimeter_side_two(self):
        self.assertEqual(perimeter(2), 8)

    def test_perimeter_side_five(self):
        self.assertEqual(perimeter(5), 20)

    def test_perimeter_side_ten(self):
        self.assertEqual(perimeter(10), 40)

    def test_perimeter_fractional_side(self):
        self.assertEqual(perimeter(0.5), 2)

    def test_perimeter_negative_side(self):
        with self.assertRaises(ValueError):
            perimeter(-5)

    def test_perimeter_string(self):
        with self.assertRaises(TypeError):
            perimeter("5")

    def test_perimeter_none(self):
        with self.assertRaises(TypeError):
            perimeter(None)
