# 5 x 4 x 3 x 2 x 1
# 1 x 4 x 3 x 2 x 1
def fact(num):
    i = 0
    fact = 1
    while i != num:
         fact = fact * (num - i)
         i = i + 1
    return fact



list = [1,2,3,4,5]

sum = 0
for i in list:
    sum = sum + fact(i)
print(f'sum of factorial of the list:{sum}')



