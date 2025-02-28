s:str = input("Enter the string:")

palindrom = False
for i in range(len(s)-1):
    if s[i] == s[len(s)-1-i]:
        palindrom = True
    else:
        palindrom = False

if palindrom:
    print('yes')
else:
    print('No')