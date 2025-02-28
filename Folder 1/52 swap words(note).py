word: str = input("Enter the word:")


char = []
for i in word.split(" "):
    char.append(i)

print(char)
len1 = len(char)
char[0],char[len1 // 2],char[-1] = char[-1], char[len1 // 2][::-1],char[0]
print(" ".join(char))




