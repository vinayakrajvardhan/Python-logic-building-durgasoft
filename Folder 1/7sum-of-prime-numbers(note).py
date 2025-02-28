num: int = int(input("Enter the number:"))
prime_number = False

sum = 0

while num > 0:
    rem = num % 10
    if rem == 2 or rem == 3 or rem == 5 or rem == 7:
        sum += rem
    num = num // 10
print(sum)
