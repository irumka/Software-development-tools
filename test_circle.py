import unittest
from circle import area, perimeter


class CircleTestCase(unittest.TestCase):

    def test_area_zero(self):
        self.assertAlmostEqual(area(0), 0.0)

    def test_area_unit_radius(self):
        self.assertAlmostEqual(area(1), 3.141592653589793)

    def test_area_radius_two(self):
        self.assertAlmostEqual(area(2), 12.566370614359172)

    def test_area_radius_three(self):
        self.assertAlmostEqual(area(3), 28.274333882308138)

    def test_area_fractional_radius(self):
        self.assertAlmostEqual(area(0.5), 0.7853981633974483)

    def test_area_negative_radius(self):
        with self.assertRaises(ValueError):
            area(-1)

    def test_area_string(self):
        with self.assertRaises(TypeError):
            area("5")

    def test_area_none(self):
        with self.assertRaises(TypeError):
            area(None)

    def test_perimeter_zero(self):
        self.assertAlmostEqual(perimeter(0), 0.0)

    def test_perimeter_unit_radius(self):
        self.assertAlmostEqual(perimeter(1), 6.283185307179586)

    def test_perimeter_radius_two(self):
        self.assertAlmostEqual(perimeter(2), 12.566370614359172)

    def test_perimeter_radius_three(self):
        self.assertAlmostEqual(perimeter(3), 18.84955592153876)

    def test_perimeter_fractional_radius(self):
        self.assertAlmostEqual(perimeter(0.5), 3.141592653589793)

    def test_perimeter_negative_radius(self):
        with self.assertRaises(ValueError):
            perimeter(-1)

    def test_perimeter_string(self):
        with self.assertRaises(TypeError):
            perimeter("5")

    def test_perimeter_none(self):
        with self.assertRaises(TypeError):
            perimeter(None)
