s = "hello123"
alp = "abcdefghijklmnopqrstuvwxyz"
final = []
for i in s:
    if i in alp:
        print(i,end=" ")

print()

for i in range(len(s)):
    print(s[i],i)

