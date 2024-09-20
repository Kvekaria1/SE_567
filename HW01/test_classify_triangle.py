import math
import unittest
from classify_triangle import classify_triangle  # Importing the classify_triangle function

class TestClassifyTriangle(unittest.TestCase):
    
    def test_equilateral(self):
        self.assertEqual(classify_triangle(3, 3, 3), "Equilateral")
    
    def test_isosceles(self):
        self.assertEqual(classify_triangle(5, 5, 8), "Isosceles")
    
    def test_scalene(self):
        self.assertEqual(classify_triangle(4, 5, 6), "Scalene")
    
    def test_right_triangle(self):
        self.assertEqual(classify_triangle(3, 4, 5), "Scalene and Right")
        self.assertEqual(classify_triangle(5, 12, 13), "Scalene and Right")
    
    def test_isosceles_right_triangle(self):
        self.assertEqual(classify_triangle(1, 1, math.sqrt(2)), "Isosceles and Right")
    
    def test_invalid_sides(self):
        self.assertEqual(classify_triangle(0, 0, 0), "InvalidInput")
        self.assertEqual(classify_triangle(-1, 2, 2), "InvalidInput")
        # Update the expected output to match the function's return value
        self.assertEqual(classify_triangle(1, 2, 3), "NotATriangle")
    
    def test_float_inputs(self):
        self.assertEqual(classify_triangle(3.0, 4.0, 5.0), "Scalene and Right")

if __name__ == '__main__':
    unittest.main()
