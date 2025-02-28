def prime_number(num):
    factor = 0
    for i in range(1, num + 1):
        if num % i == 0:
            factor = factor + 1
    return factor == 2


list = [4, 5, 7, 11, 13]
sum = 0
for i in list:
    if prime_number(i):
        sum = sum + i
print(f'sum of prime number in list:{sum}')
