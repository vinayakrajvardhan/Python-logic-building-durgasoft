num = list(input("Enter the number"))
value = []


for i in num:
    if int(i) == 2 or int(i) == 5 or int(i) == 7:
        value.append(int(i))

print(sum(value))





