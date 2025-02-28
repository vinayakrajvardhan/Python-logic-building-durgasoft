import math


def perfect_square(num):
    z = round(math.pow(num, 1 / 2))

    return num == z * z


num = 655
while True:
    if perfect_square(num):

        print(f'{num} : Yes it is perfect square')
        break
    else:
        num = num + 1


