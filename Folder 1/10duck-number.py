num = list(input("Enter the number:"))
print(num)

if num[0] != '0' and '0' in num:
    print('Duck-number')
else:
    print('octal-number')