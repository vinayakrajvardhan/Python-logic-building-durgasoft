print(ord('a'))
print(chr(97))

str = input("Enter the string:")
z = 0
m = ''
list = []
for i in str:
    z = ord(i) + 1
    list.append(z)
print(list)

for j in list:
    print(chr(j), end=" ")


