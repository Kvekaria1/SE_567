import math

def classify_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Invalid: Sides must be greater than 0"
    if a + b <= c or a + c <= b or b + c <= a:
        return "Invalid: Not a valid triangle"  # Updated this return value
    
    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        triangle_type = "Isosceles"
    else:
        triangle_type = "Scalene"
    
    sides = sorted([a, b, c])
    if math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2):
        triangle_type += " and Right"
    
    return triangle
