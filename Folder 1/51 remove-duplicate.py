word:str = input("Enter the word:")

char = []

for i in word:
    if i not in char:
        char.append(i)
print(char)