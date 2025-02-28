word:str = input("Enter the word:")

vowels = ['a','i','e','o','u']

for i in range(len(word)):
    if word[i] in vowels:
        print(i,word[i])
        break