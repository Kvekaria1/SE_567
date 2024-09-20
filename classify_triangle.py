def classify_triangle(a, b, c):
    # Check if inputs are valid (positive numbers and form a triangle)
    if a <= 0 or b <= 0 or c <= 0:
        return "InvalidInput"
    
    if a + b <= c or a + c <= b or b + c <= a:
        return "NotATriangle"
    
    # Determine triangle type by comparing side lengths
    if a == b and b == c:
        triangle_type = "Equilateral"
    elif a == b or b == c or a == c:
        triangle_type = "Isosceles"
    else:
        triangle_type = "Scalene"
    
    # Check if it's a right triangle using Pythagoras' theorem
    if round(a**2 + b**2, 5) == round(c**2, 5) or \
       round(a**2 + c**2, 5) == round(b**2, 5) or \
       round(b**2 + c**2, 5) == round(a**2, 5):
        triangle_type += " and Right"
    
    return triangle_type
