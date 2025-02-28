list = [1, 8, 4, 5, 7, 2]
m =[]
for i in range(1,len(list)-1):
    l = i -1
    r = i + 1
    if list[i -1] < list[i] and list[i] > list[i + 1]:
        m.append(list[i])

print(m)