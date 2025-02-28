def sum_of_products_with_successors(N, A):
    """
    Calculate the sum of all products with successors.

    Args:
        N (int): The length of array A.
        A (list): The input array.

    Returns:
        int: The sum of all products with successors.
    """
    total_sum = 0
    for i in range(N - 1):
        total_sum += A[i] * A[i + 1]
    return total_sum

# Test the function
N = 5
A = [1, 2, 3, 4, 5]
print("Sum of products with successors:", sum_of_products_with_successors(N, A))
