#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a given n x n 2D matrix 90 degrees clockwise in place.

    Args:
        matrix (list of list of int): A 2D matrix to rotate.

    Returns:
        None: The matrix is modified in-place.
    """
    n = len(matrix)

    # Transpose the matrix (swap rows with columns)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i].reverse()