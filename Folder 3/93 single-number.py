list = [1,1,1,2,2,2,3,4,4,4,4,4,4]
d = {}

for i in list:
    if i not in d:
        d[i] = 1
        c = 1
    else:
        d[i] = d[i] + 1
        c = c +1

print(d)

for i,j in d.items():
    if j == 1:
        print(f'unique value is {i}')



