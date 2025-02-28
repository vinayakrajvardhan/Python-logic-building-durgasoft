def is_prime(num:int):
    factor = 0
    for i in range(1,num+1):
        if num % i == 0:
            factor =  factor + 1
    return factor == 2

num1:int = int(input("Enter the first number:"))
# print(is_prime(num1))

while True:
   if is_prime(num1):
       print(num1)
       break
   else:
       num1 = num1 + 1
