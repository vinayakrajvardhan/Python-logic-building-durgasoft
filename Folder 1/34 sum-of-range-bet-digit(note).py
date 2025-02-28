def sum_digits(num:int):
    sum = 0
    while num != 0:
        rem = num % 10
        sum += rem
        num = num // 10
    return sum


num1: int = int(input("Enter the first number:"))
num2: int = int(input("Enter the second number:"))
# print(sum_digits(num1))


z = 0
for i in range(num1,num2+1):
    z = z + sum_digits(i)
print(z)







