word:str = input("Enter the word")
if len(word) % 2 == 0:
    print(word[len(word)//2 - 1])
else:
    print(word[len(word)//2])


