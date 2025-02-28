amount = list(input("Enter the amount"))

sum = 0

for i in range(len(amount)):
    if i % 2 != 0:
        sum+=int(amount[i])
print(f'sum of amount is {sum}')

