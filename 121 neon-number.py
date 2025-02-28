#  9 = 9*9 = 81 , 8+1 = 9
import math


def sum_of_number(num):
    sum = 0
    while num != 0:
        d = num % 10
        sum = sum + d
        num = num // 10
    return sum


def neon_number(num):
    z = math.pow(num, 1 / 2)
    r = sum_of_number(z)
    return r * r == num


print(f'Number is neon: {neon_number(81)}')
