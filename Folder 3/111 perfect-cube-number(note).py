import math


def perfect_cube(num):

    z = round(math.pow(num,1/3))

    return z * z * z == num

print(perfect_cube(28))