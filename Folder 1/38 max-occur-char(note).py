word:str = input("Enter the word:")
char = {}

for i in word:
    if i not in char:
        char[i] = 1
    else:
        char[i] = char[i] + 1

print(char)
print(max(char,key=char.get))



