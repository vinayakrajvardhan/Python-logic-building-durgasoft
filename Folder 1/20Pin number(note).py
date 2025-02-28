def generate_pin(num1, num2, num3):
    # Extract the digits from the input numbers
    digits1 = [int(d) for d in str(num1)]
    digits2 = [int(d) for d in str(num2)]
    digits3 = [int(d) for d in str(num3)]

    # Find the least of the units, tens, and hundreds positions
    units = min(digits1[2], digits2[2], digits3[2])
    tens = min(digits1[1], digits2[1], digits3[1])
    hundreds = min(digits1[0], digits2[0], digits3[0])

    # Find the max of all digits in the three input numbers
    max_digit = max(max(digits1), max(digits2), max(digits3))

    # Construct the PIN
    pin = f"{max_digit}{hundreds}{tens}{units}"

    return pin
num1 = 123
num2 = 456
num3 = 789

pin = generate_pin(num1, num2, num3)
print(f"Generated PIN: {pin}")