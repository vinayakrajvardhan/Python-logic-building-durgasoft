num: int = int(input("Enter the number:"))
c = 0

while num > 0:
    rem = num % 10
    c += 1
    num = num // 10
print(c)
