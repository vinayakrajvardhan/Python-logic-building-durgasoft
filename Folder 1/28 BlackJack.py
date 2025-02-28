


def blackJack(num1,num2,num):
    z1 = abs(num1-num)
    z2 = abs(num2-num)
    if z1 > z2:
        return f'Number closer to {num} is:{num2}'
    else:
        return f'Number closer to {num} is:{num1}'



num1:int = int(input("Enter the first number:"))
num2:int = int(input("Enter the second number:"))
num:int = int(input("Enter the number to check:"))
print(blackJack(num1,num2,num))