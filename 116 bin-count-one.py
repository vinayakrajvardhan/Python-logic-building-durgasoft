num = 123
c = 0
print(bin(num))
for i in bin(num):
    if i == '1':
        c = c + 1
print(c)