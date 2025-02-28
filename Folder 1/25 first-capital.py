letter = input("Enter the number:")


for i in range(len(letter)):
    if letter[i].isupper():
        print(f'First capital letter is {letter[i]} at index {i}')



