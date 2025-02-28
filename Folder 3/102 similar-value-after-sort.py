L1 = [1,2,3,4,5,6,8,7,2,3]

L2 = L1[:]
L2.sort()
print(L2)

c = 0
for i in range(len(L1)):
    if L1[i] == L2[i]:
        c = c + 1

print(f'Total number of element at the same place after sort:{c}')
