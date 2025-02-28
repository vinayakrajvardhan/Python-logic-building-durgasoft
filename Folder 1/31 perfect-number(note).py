def perfect_number(num:int):
    sum = 0
    for i in range(1,num):
        if num % i == 0:
            sum += i
            print(i,end=" ")
    return sum == num

num1:int = int(input("Enter the first number:"))

print(perfect_number(num1))