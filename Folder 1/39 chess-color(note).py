def square_color(coordinates):
    # Convert the coordinates to a format that's easier to work with
    letter = coordinates[0]
    number = int(coordinates[1])

    # Calculate the row and column numbers (1-8)
    row = number
    column = ord(letter) - ord('a') + 1

    # Check if the square is white or black
    if (row + column) % 2 == 0:
        return True  # White
    else:
        return False  # Black

print(square_color('a1'))  # True (white)
print(square_color('h8'))  # False (black)
print(square_color('d4'))  # True (white)
print(square_color('e5'))  # False (black)