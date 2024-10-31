# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""


def classify_triangle(a, b, c):
    """
    Function to classify the type of triangle based on the lengths of its sides.
    It returns one of the following strings: 'Equilateral', 'Isoceles', 'Scalene',
    'NotATriangle', or 'Right'.
    """
    # Check for invalid inputs
    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'
    
    # Check if it is not a triangle
    if a + b <= c or a + c <= b or b + c <= a:
        return 'NotATriangle'
    
    # Check for equilateral triangle
    if a == b == c:
        return 'Equilateral'
    
    # Check for isosceles triangle
    if a == b or b == c or a == c:
        # Check for a right triangle as well
        if (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
            return 'Right and Isosceles'
        return 'Isosceles'  # Ensure correct spelling here
    
    # Check for right triangle
    if (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
        return 'Right'
    
    # If it is not equilateral, isosceles, or right, it must be scalene
    return 'Scalene'
