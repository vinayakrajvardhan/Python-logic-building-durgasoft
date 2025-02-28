def prime_number(num):
    factor = 0
    for i in range(1,num + 1):
        if num % i == 0:
            factor += 1

    return factor == 2


list = [2,4,5,6,7,8]
for i in list:
    if prime_number(i):
        print(f'prime number in list is {i}')

