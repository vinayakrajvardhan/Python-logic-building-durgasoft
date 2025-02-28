str = 'vinayak'

vowels = ['a','e','i','o','u']
z = []

for i in str:
    if i in vowels:
        z.append(chr(ord(i) + 1))
    else:
        z.append(i)

print("".join(z))


