def prime_number(num):
    factor = 0
    for i in range(1,num + 1):
        if num % i == 0:
            factor = factor + 1
    return factor == 2

list = [11,13,17,2,5]
prime = False
for i in list:
    if prime_number(i):
        prime = True
    else:
        prime = False

if prime:
    print('Prime array list')
else:
    print('Not Prime array list')
