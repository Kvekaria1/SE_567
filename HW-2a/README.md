
# Triangle Classification Program

## Overview

This project implements a Python program that classifies triangles based on the lengths of their sides. The program includes a function `classifyTriangle(a, b, c)` that returns the type of triangle given three integer side lengths. The possible classifications are:
- **Equilateral**: All three sides are equal.
- **Isosceles**: Exactly two sides are equal.
- **Scalene**: All sides are different.
- **Right**: The sum of the squares of two sides equals the square of the third side (Pythagorean theorem).
- **NotATriangle**: The input does not satisfy the triangle inequality theorem (the sum of any two sides must be greater than the third).
- **InvalidInput**: The input is invalid if any side length is less than or equal to 0, greater than 200, or not an integer.

Additionally, a set of unit tests is provided in `TestTriangle.py` to verify the correctness of the function.

## Files

- **Triangle.py**: Contains the `classifyTriangle()` function that classifies triangles based on the side lengths.
- **TestTriangle.py**: Contains unit tests for `classifyTriangle()` to ensure that all edge cases and classifications are handled correctly.

## Requirements

- Python 3.x
- `unittest` library (which comes pre-installed with Python)

## Running the Program

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. To test the program, navigate to the project directory and run:
   ```bash
   python -m unittest TestTriangle
   ```

3. If all tests pass, you will see an output like:
   ```
   Ran 9 tests in 0.001s
   OK
   ```

## Test Coverage

The following test cases are included in the `TestTriangle.py` file:

1. **Equilateral Triangle Test**: Tests that a triangle with all equal sides is classified as equilateral.
2. **Right Triangle Test**: Tests that triangles that satisfy the Pythagorean theorem are classified as right triangles.
3. **Isosceles Triangle Test**: Tests that triangles with two equal sides are classified as isosceles.
4. **Scalene Triangle Test**: Tests that triangles with all different side lengths are classified as scalene.
5. **Invalid Triangle Test**: Tests that invalid triangles (those that don’t meet the triangle inequality) are correctly classified as not a triangle.
6. **Negative and Zero Side Length Tests**: Tests that negative and zero-length sides are considered invalid input.
7. **Large Side Length Test**: Tests that side lengths larger than 200 are considered invalid input.

## Author
- Krish Vekaria

## License

This project is licensed under the MIT License. See the LICENSE file for details.
