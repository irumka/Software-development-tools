import unittest
from circle import area, perimeter


class CircleTestCase(unittest.TestCase):

    def test_area_zero(self):
        res = area(0)
        self.assertAlmostEqual(res, 0.0)

    def test_area_radius_one(self):
        res = area(1)
        self.assertAlmostEqual(res, 3.141592653589793)

    def test_area_radius_two(self):
        res = area(2)
        self.assertAlmostEqual(res, 12.566370614359172)

    def test_area_radius_three(self):
        res = area(3)
        self.assertAlmostEqual(res, 28.274333882308138)

    def test_area_fractional_radius(self):
        res = area(0.5)
        self.assertAlmostEqual(res, 0.7853981633974483)

    def test_perimeter_zero(self):
        res = perimeter(0)
        self.assertAlmostEqual(res, 0.0)

    def test_perimeter_radius_one(self):
        res = perimeter(1)
        self.assertAlmostEqual(res, 6.283185307179586)

    def test_perimeter_radius_two(self):
        res = perimeter(2)
        self.assertAlmostEqual(res, 12.566370614359172)

    def test_perimeter_radius_three(self):
        res = perimeter(3)
        self.assertAlmostEqual(res, 18.84955592153876)

    def test_perimeter_fractional_radius(self):
        res = perimeter(0.5)
        self.assertAlmostEqual(res, 3.141592653589793)