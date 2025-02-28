def recursive_sum(num):
    sum = 0
    while num!=0:
        sum = sum + num%10
        num = num // 10
    return sum


print(recursive_sum(123))
