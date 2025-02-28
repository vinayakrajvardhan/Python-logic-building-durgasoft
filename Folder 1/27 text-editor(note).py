def count_misses(text):
    # Initialize a counter for misses
    misses = 0

    # Iterate over each character in the input string
    for char in text:
        # Check if the character is not an English letter, number, or whitespace
        if not (char.isalpha() or char.isdigit() or char.isspace()):
            # Increment the misses counter
            misses += 1

    # Return the total number of misses
    return misses


# Example usage:
text = "Hello, World! 123"
misses = count_misses(text)
print(f"Number of misses: {misses}")