def matrix_to_array(matrix):
    """
    Converts a given matrix into an array.

    Args:
        matrix (list): The matrix to convert.

    Returns:
        list: The resulting array.
    """
    return [element for row in matrix for element in row]

# Test the function
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

array = matrix_to_array(matrix)
print("Matrix:")
for row in matrix:
    print(row)
print("Array:", array)