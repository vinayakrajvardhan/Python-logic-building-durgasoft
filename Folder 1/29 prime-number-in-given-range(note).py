num1:int = int(input("Enter the first number:"))
num2:int = int(input("Enter the second number:"))


def prime_number(num):
   factor = 0
   for i in range(1,num+1):
       if num % i == 0:
           factor = factor + 1
   return factor == 2

sum = 0
for i in range(num1,num2+1):
    if prime_number(i):
        sum = sum + i
print(sum)











