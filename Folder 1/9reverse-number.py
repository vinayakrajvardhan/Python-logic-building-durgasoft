num: int = int(input("Enter the number:"))
number = []
while num > 0:
    rem = num % 10
    print(f'Reverse number :{rem}',end="")
    num = num // 10

