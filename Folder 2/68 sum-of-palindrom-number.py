def palindrom(num:str):
    if num == num[::-1]:
        return num

list = [121,221,343]
sum = 0
for i in list:
    if palindrom(str(i)):
        sum = sum + i
        print(i,end=" ")
print()
print(f'sum of palindrom number in list:{sum}')
