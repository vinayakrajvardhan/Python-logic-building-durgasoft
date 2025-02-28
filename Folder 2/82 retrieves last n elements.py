def get_last_n_elements(lst, n):
    return lst[-n:]

# Test the function
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
last_three_elements = get_last_n_elements(numbers, 3)
print(last_three_elements)  # Output: [7, 8, 9]