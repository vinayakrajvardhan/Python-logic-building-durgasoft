
def is_happy_number(n):
    """
    Determine whether a number is a happy number or not.

    Args:
        n (int): The input number.

    Returns:
        bool: True if the number is a happy number, False otherwise.
    """
    def get_digits_sum(num):
        return sum(int(digit) ** 2 for digit in str(num))

    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = get_digits_sum(n)

    return n == 1

# Test the function
print(is_happy_number(19))  # True
print(is_happy_number(20))  # False


