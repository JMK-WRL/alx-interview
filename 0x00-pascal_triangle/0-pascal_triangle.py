#!/usr/bin/python3
"""
Module: pascal_triangle

Contains a function to generate Pascal's triangle up to a specified number of rows.
"""

def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the specified number of rows.

    Parameters:
        n (int): The number of rows in Pascal's triangle.

    Returns:
        list: A list of lists representing Pascal's triangle. Each inner list represents a row of the triangle,
              and contains the corresponding integers.

        If n <= 0, returns an empty list.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize with the first row containing a single element, 1

    # Generate each row of Pascal's triangle
    for i in range(1, n):
        row = [1]  # Start each row with 1
        for j in range(1, i):
            # Calculate the value of each element in the row using the values from the previous row
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # End each row with 1
        triangle.append(row)  # Add the generated row to the triangle

    return triangle

