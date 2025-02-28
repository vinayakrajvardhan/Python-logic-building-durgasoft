s:str = input("Enter the string:")

palindrom = False
i = 0

while i < len(s) -1:
    if s[i] == s[len(s)-1-i]:
        i+=1
        palindrom = True
        break
    else:
        palindrom = False
        break

if palindrom:
    print('Yes')
else:
    print('No')