list = [1, 2, 3, 4, 5, 6, 7, 8]
sum = 0
for i in range(len(list)):
    sum = sum + list[i] + list[-i - 1]
print(sum)
