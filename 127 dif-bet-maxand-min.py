num = '432815'

def max_number(num):
    for i in range(len(num)):
        max = num[i]
        for j in range(len(num) - 1):
            if num[j] > max:
                max = num[j]
        return max

def min_number(num):
    for i in range(len(num)):
        min = num[i]
        for j in range(len(num) - 1):
            if num[j] < min:
                min = num[j]
        return min


print(int(max_number(num)))
print(int(min_number(num)))
print(f'difference between max and min is:{int(max_number(num)) - int(min_number(num))} ')
