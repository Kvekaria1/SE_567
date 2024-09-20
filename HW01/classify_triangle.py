def classify_triangle(a, b, c):
    # First, check if the input values form a valid triangle
    if a + b <= c or b + c <= a or a + c <= b:
        return "Not a triangle"

    # Check for equilateral triangle
    if a == b == c:
        return "Equilateral"

    # Check for right triangle using the Pythagorean theorem
    if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
        return "Right"

    # Check for isosceles triangle
    if a == b or b == c or a == c:
        return "Isosceles"

    # If none of the above, it's a scalene triangle
    return "Scalene"
