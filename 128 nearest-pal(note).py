def nearest_palindrome(n):
    def is_palindrome(num):
        return str(num) == str(num)[::-1]

    lower = upper = n
    while True:
        if is_palindrome(lower):
            return lower
        if is_palindrome(upper):
            return upper
        lower -= 1
        upper += 1

# Test the function
print(nearest_palindrome(123))  # 121
print(nearest_palindrome(456))  # 454
print(nearest_palindrome(1000))  # 1001