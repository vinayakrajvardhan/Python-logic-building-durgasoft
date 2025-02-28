paper = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6}

roll_number = int(input('Enter the roll number'))
sum = 0

while roll_number != 0:
    sum = sum + roll_number % 10
    roll_number = roll_number // 10

print(sum)

for key,value in paper.items():
    if sum == value:
        print(f'question set:{key}')