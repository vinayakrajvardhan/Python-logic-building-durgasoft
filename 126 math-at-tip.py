num = '12345'
k = 2

a = []
c = 0

for i in num:
    if k == int(i):
        continue
    c = c + 1
    a.append(i)

print(c)
print(a)
