str = input("Enter the string:")

vowels = {'@':'a','#':'e','$':'i','%':'o','^':'u'}
r = []
for i in str:
     if i not in vowels.keys():
        r.append(i)
     else:
        r.append(vowels[i])

print(" ".join(r))
