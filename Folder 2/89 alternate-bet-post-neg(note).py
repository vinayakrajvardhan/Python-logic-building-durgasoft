list = [1,-2,3,-4,5,-6,7,-8,9]

negative_number = []

for i in range(len(list)):
    if i % 2 != 0:
        negative_number.append(list[i])
value = False
for i in negative_number:
    if i < 0:
        value = True
    else:
        value = False

if value:
    print('Negative number alternate')
else:
    print('Not negative number alternate')