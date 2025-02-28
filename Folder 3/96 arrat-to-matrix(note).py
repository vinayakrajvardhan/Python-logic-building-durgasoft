def array_to_matrix(arr, rows, cols):
    """
    Converts a one-dimensional array into a two-dimensional matrix.

    Args:
        arr (list): The one-dimensional array to convert.
        rows (int): The number of rows in the resulting matrix.
        cols (int): The number of columns in the resulting matrix.

    Returns:
        list: The resulting two-dimensional matrix.
    """
    if len(arr) != rows * cols:
        raise ValueError("Array length does not match matrix dimensions")

    matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    index = 0

    for i in range(rows):
        for j in range(cols):
            matrix[i][j] = arr[index]
            index += 1

    return matrix

# Test the function
arr = [1, 2, 3, 4, 5, 6]
rows = 2
cols = 3

matrix = array_to_matrix(arr, rows, cols)
for row in matrix:
    print(row)

#
# This program defines a function array_to_matrix that takes a one-dimensional array arr, the number of rows rows, and the number of columns cols as input. It checks if the length of the array matches the matrix dimensions and raises a ValueError if they do not match.
#
# The function then creates an empty matrix with the specified number of rows and columns and fills it with the elements of the array.
#
# Finally, the function returns the resulting matrix.
#
# When you run this program with the provided array, rows, and columns, it will output:


[1, 2, 3]
[4, 5, 6]