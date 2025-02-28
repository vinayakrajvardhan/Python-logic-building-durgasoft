def is_magic_date(mm, dd, yyyy):
    # Calculate the product of mm and dd
    product = mm * dd

    # Convert the product to a string
    product_str = str(product)

    # Convert the last digits of yyyy to a string
    year_str = str(yyyy)

    # Check if the product matches the last digits of yyyy
    if len(product_str) == 1 and product_str == year_str[-1]:
        return True
    elif len(product_str) == 2 and product_str == year_str[-2:]:
        return True
    elif len(product_str) == 3 and product_str == year_str[-3:]:
        return True
    else:
        return False


def main():
    # Read the date, month, and year from the user
    mm = int(input("Enter the month (1-12): "))
    dd = int(input("Enter the day (1-31): "))
    yyyy = int(input("Enter the year: "))

    # Check if the date is a magic date
    if is_magic_date(mm, dd, yyyy):
        print(f"{mm}/{dd}/{yyyy} is a magic date!")
    else:
        print(f"{mm}/{dd}/{yyyy} is not a magic date.")


if __name__ == "__main__":
    main()

