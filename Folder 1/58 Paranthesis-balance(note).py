s = input("Enter the word:")
c = 0
for i in s:
    if i == '(':
        c = c + 1
if i == ')':
    c = c - 1
print(c)
