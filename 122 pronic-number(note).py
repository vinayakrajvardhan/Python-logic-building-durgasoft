import math

def is_pronic_number(n):
    for i in range(1, int(math.sqrt(n)) + 1):
        if i * (i + 1) == n:
            return True
    return False

# Test the function
print(is_pronic_number(2))  # True
print(is_pronic_number(6))  # True
print(is_pronic_number(12))  # True
print(is_pronic_number(20))  # True
print(is_pronic_number(30))  # True
print(is_pronic_number(10))  # False