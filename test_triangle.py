import unittest
from triangle import area, perimeter

class TriangleTestCase(unittest.TestCase):

    def test_area_1(self):
        res = area(6, 0)
        self.assertEqual(res, 0.0)

    def test_area_2(self):
        res = area(0, 5)
        self.assertEqual(res, 0.0)

    def test_area_3(self):
        res = area(6, 4)
        self.assertEqual(res, 12.0)

    def test_area_4(self):
        res = area(1, 1)
        self.assertEqual(res, 0.5)

    def test_area_5(self):
        res = area(10, 10)
        self.assertEqual(res, 50.0)

    def test_perimeter_1(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_perimeter_2(self):
        res = perimeter(3, 4, 5)
        self.assertEqual(res, 12)

    def test_perimeter_3(self):
        res = perimeter(2, 2, 2)
        self.assertEqual(res, 6)

    def test_perimeter_4(self):
        res = perimeter(5, 5, 8)
        self.assertEqual(res, 18)

    def test_perimeter_5(self):
        res = perimeter(1, 1, 1)
        self.assertEqual(res, 3)