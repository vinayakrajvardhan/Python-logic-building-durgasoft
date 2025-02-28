num:int = input("Enter the number")


sum = 0
product = 1
for i in num:
    sum += int(i)
    product*= int(i)
print(sum)
print(product)

print((sum + product) == int(num))


