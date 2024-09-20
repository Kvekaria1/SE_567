import unittest
from classify_triangle import classify_triangle

class TestClassifyTriangle(unittest.TestCase):

    def test_equilateral(self):
        self.assertEqual(classify_triangle(3, 3, 3), "Equilateral")

    def test_isosceles(self):
        self.assertEqual(classify_triangle(5, 5, 3), "Isosceles")
        self.assertEqual(classify_triangle(5, 3, 5), "Isosceles")
        self.assertEqual(classify_triangle(3, 5, 5), "Isosceles")

    def test_scalene(self):
        self.assertEqual(classify_triangle(3, 4, 5), "Right")  # Right triangle is also Scalene
        self.assertEqual(classify_triangle(6, 7, 8), "Scalene")

    def test_right(self):
        self.assertEqual(classify_triangle(3, 4, 5), "Right")
        self.assertEqual(classify_triangle(5, 12, 13), "Right")
        self.assertEqual(classify_triangle(8, 15, 17), "Right")

    def test_invalid_triangle(self):
        self.assertEqual(classify_triangle(1, 2, 3), "Not a triangle")
        self.assertEqual(classify_triangle(5, 1, 1), "Not a triangle")

    def test_zero_or_negative_sides(self):
        self.assertEqual(classify_triangle(0, 5, 5), "Not a triangle")
        self.assertEqual(classify_triangle(-1, 4, 5), "Not a triangle")

if __name__ == '__main__':
    unittest.main()
