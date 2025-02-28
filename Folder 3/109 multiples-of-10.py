list = [10, 11, 20, 15, 30, 45, 50]
n = []
m = []
for i in range(len(list)):
    if list[i] % 10 == 0:
        n.append(list[i])
    else:
        m.append(list[i])

print(m + n)
