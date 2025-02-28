num1:int = int(input("Enter the number:"))
num:int = num1
sum = 0
product = 1
while  num > 0:
    rem = num % 10
    sum += rem
    product *= rem
    num = num // 10
print(f'sum of number is :{sum}')
print(f'product of number is :{product}')
print((sum + product) == num1)
