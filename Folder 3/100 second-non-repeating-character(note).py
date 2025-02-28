


def second_non_repeating_char(arr):
    char_count = {}

    # Count the occurrence of each character
    for char in arr:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    print(char_count)
    # Find the second non-repeating character
    non_repeating_chars = [char for char, count in char_count.items() if count == 1]
    print(non_repeating_chars)
    if len(non_repeating_chars) < 2:
        return None
    else:
        return non_repeating_chars[1]


# Test the function
arr = ['a', 'b', 'c', 'a', 'd', 'd']
print("Second non-repeating character:", second_non_repeating_char(arr))
