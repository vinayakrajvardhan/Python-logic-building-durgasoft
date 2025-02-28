def prime_number(num):
    factor = 1
    for i in range(2,num+1):
        if num % i == 0:
            factor += 1
    return factor == 2


print(prime_number(97))

for i in range(1,100):
    if prime_number(i):
        print(i,end=" ,")