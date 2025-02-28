word:str = input("Enter the word:")

vowels = ['a','i','e','o','u']

repl = []

for i in word:
    if i not in vowels:
        repl.append(i)


print(repl)