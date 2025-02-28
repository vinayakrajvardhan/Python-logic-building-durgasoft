def longest_word(s):
    words = s.split()
    longest = max(words, key=len)
    return longest

# Test the function
s = "This is a test sentence with a really long word"
print(longest_word(s))