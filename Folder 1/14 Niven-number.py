num = int(input("Ente the number"))

sum = 0


while num > 0:
    rem = num % 10
    sum += rem
    num = num // 10
print(sum)
print('yes' if num//sum == 0 else 'no')
