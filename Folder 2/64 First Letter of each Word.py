str = 'The quick brown fox jumps over the lazy dog'

z = str.split(" ")
print(z,end=" ")
print()
for i in range(len(z)):
    print(z[i][0],end=" ")