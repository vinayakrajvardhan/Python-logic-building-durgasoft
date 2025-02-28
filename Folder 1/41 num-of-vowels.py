word:str = input("Enter the word:")

vowels = ['a','i','e','o','u']

count = []

for i in word:
    if i in vowels:
        count.append(i)

print(len(count))