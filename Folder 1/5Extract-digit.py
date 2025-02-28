num: int = int(input("Enter the number:"))

sum  = 0

while num > 0:
    rem = num % 10
    print(rem, end="")
    sum += rem
    num = num // 10
print()
print(f'sum of number :{sum}')
