list = [1, 2, 3, 4, 5, 6]

consecutive_number = False
for i in range(len(list) - 1):
    if list[i + 1] - list[i] == 1:
        consecutive_number = True
    else:
        consecutive_number = False

if consecutive_number:
    print(f'number is consecutive')
else:
    print(f'number is not consecutive')
