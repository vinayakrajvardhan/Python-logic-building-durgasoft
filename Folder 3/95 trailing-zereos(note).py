def trailing_zeros(num: int):
    count = 0
    while num != 0:
        if num % 10 == 0:
            count += 1
        else:
            break
        num = num // 10
    return count

num = 1200
print(f'Trailling zeroes in {num}:{trailing_zeros(num)}')
