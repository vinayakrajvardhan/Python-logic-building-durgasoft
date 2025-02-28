


def process_numbers():
    numbers = []
    while True:
        num = int(input("Enter a number (-ve to stop): "))
        if num < 0:
            break
        numbers.append(num)

    processed_numbers = []
    for num in numbers:
        last_digit = num % 10
        if num < 50 and last_digit == 2:
            processed_numbers.append(-6)
        elif last_digit == 2:
            processed_numbers.append(-1)
        elif num < 50:
            processed_numbers.append(-5)
        else:
            processed_numbers.append(num)

    print("Original numbers:", numbers)
    print("Processed numbers:", processed_numbers)

if __name__ == "__main__":
    process_numbers()
