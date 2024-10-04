# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""


def classifyTriangle(a, b, c):
    """
    Function to classify the type of triangle based on the lengths of its sides.
    It returns one of the following strings: 'Equilateral', 'Isoceles', 'Scalene', 'NotATriangle', or 'Right'.
    """

    # Input validation
    if a > 200 or b > 200 or c > 200 or a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'

    # Check if inputs are integers
    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return 'InvalidInput'

    # Check if it's a valid triangle using the triangle inequality
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return 'NotATriangle'

    # Check if it's an equilateral triangle
    if a == b == c:
        return 'Equilateral'

    # Check if it's a right triangle using Pythagoras theorem
    if (a ** 2 + b ** 2 == c ** 2) or (a ** 2 + c ** 2 == b ** 2) or (b ** 2 + c ** 2 == a ** 2):
        return 'Right'

    # Check if it's an isosceles triangle
    if a == b or b == c or a == c:
        return 'Isoceles'

    # Otherwise, it must be a scalene triangle
    return 'Scalene'
