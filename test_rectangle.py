import unittest
from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):

    def test_area_1(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_area_2(self):
        res = area(1, 1)
        self.assertEqual(res, 1)

    def test_area_3(self):
        res = area(3, 4)
        self.assertEqual(res, 12)

    def test_area_4(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_area_5(self):
        res = area(1000, 2)
        self.assertEqual(res, 2000)

    def test_perimeter_1(self):
        res = perimeter(10, 0)
        self.assertEqual(res, 20)

    def test_perimeter_2(self):
        res = perimeter(1, 1)
        self.assertEqual(res, 4)

    def test_perimeter_3(self):
        res = perimeter(3, 4)
        self.assertEqual(res, 14)

    def test_perimeter_4(self):
        res = perimeter(10, 10)
        self.assertEqual(res, 40)

    def test_perimeter_5(self):
        res = perimeter(1000, 2)
        self.assertEqual(res, 2004)