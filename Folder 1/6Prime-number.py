num: int = int(input("Enter the number:"))
prime_number =  False

for i in range(2,num):
    if num % i == 0:
        prime_number = False
    else:
        prime_number = True

if prime_number:
    print('Prime Number')
else:
    print('Not prime number')