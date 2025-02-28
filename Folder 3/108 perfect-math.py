list = [20, 23, 44, 47]
k = 3

sum = 0

for i in range(len(list)):
    sum = sum + list[i] % k
print(sum)
