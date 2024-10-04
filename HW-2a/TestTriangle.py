# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest
from Triangle import classifyTriangle


# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):

    # Test for right triangle cases
    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3, 4, 5 is a Right triangle')

    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', '5, 3, 4 is a Right triangle')

    # Test for equilateral triangle
    def testEquilateralTriangles(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1, 1, 1 should be equilateral')

    # Test for isosceles triangle
    def testIsoscelesTriangle(self):
        self.assertEqual(classifyTriangle(5, 5, 8), 'Isoceles', '5, 5, 8 should be isosceles')

    # Test for scalene triangle
    def testScaleneTriangle(self):
        self.assertEqual(classifyTriangle(3, 4, 6), 'Scalene', '3, 4, 6 should be scalene')

    # Test for invalid triangle (sum of two sides not greater than the third side)
    def testInvalidTriangle(self):
        self.assertEqual(classifyTriangle(1, 10, 12), 'NotATriangle', '1, 10, 12 should not be a triangle')

    # Test for negative sides (invalid case)
    def testNegativeSides(self):
        self.assertEqual(classifyTriangle(-1, 5, 5), 'InvalidInput', 'Negative side lengths should return InvalidInput')

    # Test for zero-length side (invalid case)
    def testZeroSides(self):
        self.assertEqual(classifyTriangle(0, 5, 5), 'InvalidInput', 'Zero side length should return InvalidInput')

    # Test for large sides greater than 200 (invalid case)
    def testLargeSides(self):
        self.assertEqual(classifyTriangle(201, 150, 150), 'InvalidInput',
                         'Sides larger than 200 should return InvalidInput')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
