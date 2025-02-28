list = ['123', '444', '553']
sum = 0
for i in list:
    if i.endswith('3'):
        sum = sum + int(i)
print(f'sum of list ending with 3:{sum}')
