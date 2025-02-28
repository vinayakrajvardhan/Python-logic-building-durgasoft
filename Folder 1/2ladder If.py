num:int = int(input("Enter the number"))

if num % 2 != 0:
    print('weird')
elif num in range(2,5) and num % 2 == 0:
    print('Not Weird')
elif num in range(6,20) and num % 2 == 0:
    print('Weird')
elif num > 20 and num % 2 == 0:
    print('Not Weird')

