# test_classify_triangle.py

import unittest
from triangle import classify_triangle

class TestTriangle(unittest.TestCase):
    """Unit tests for the classify_triangle function"""

    def test_right_triangle_a(self):
        """Test case for a right triangle with sides 3, 4, 5"""
        self.assertEqual(classify_triangle(3, 4, 5), 'Right', '3, 4, 5 is a Right triangle')

    def test_right_triangle_b(self):
        """Test case for a right triangle with sides 5, 3, 4"""
        self.assertEqual(classify_triangle(5, 3, 4), 'Right', '5, 3, 4 is a Right triangle')

    def test_equilateral_triangles(self):
        """Test case for an equilateral triangle with sides 1, 1, 1"""
        self.assertEqual(classify_triangle(1, 1, 1), 'Equilateral', '1, 1, 1 should be equilateral')

    def test_isosceles_triangle(self):
        """Test case for an Isosceles triangle with sides 5, 5, 8"""
        self.assertEqual(classify_triangle(5, 5, 8), 'Isosceles', '5, 5, 8 should be isosceles')

    def test_scalene_triangle(self):
        """Test case for a scalene triangle with sides 3, 4, 6"""
        self.assertEqual(classify_triangle(3, 4, 6), 'Scalene', '3, 4, 6 should be scalene')

    def test_invalid_triangle(self):
        """Test case for an invalid triangle with sides 1, 10, 12"""
        self.assertEqual(classify_triangle(1, 10, 12), 'NotATriangle', '1 , 10, 12 should be invalid')

    def test_negative_sides(self):
        """Test case for an invalid triangle with a negative side length"""
        self.assertEqual(classify_triangle(-1, 5, 5), 'InvalidInput', 'Negative side lengths should be InvalidInput')

    def test_zero_sides(self):
        """Test case for an invalid triangle with a side of length zero"""
        self.assertEqual(classify_triangle(0, 5, 5), 'InvalidInput', 'Zero side lengths should be InvalidInput')

    def test_large_sides(self):
        """Test case for an invalid triangle with sides larger than 200"""
        self.assertEqual(classify_triangle(201, 201, 201), 'InvalidInput', 'Sides greater than 200 should be InvalidInput')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

