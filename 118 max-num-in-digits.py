num = '432815'

for i in range(len(num)):
    max = num[i]
    for j in range(len(num) - 1):
        if num[j] > max:
            max = num[j]



print(f'Max number in digit is:{max}')
