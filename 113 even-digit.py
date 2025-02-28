# num = 1234

def even_digit(num):
    c = 0
    while num != 0:
        rev = num % 10
        if rev % 2 == 0:
            c = c + 1
        num = num // 10
    return c
num = int(input("enter the number:"))

print(even_digit(num))
