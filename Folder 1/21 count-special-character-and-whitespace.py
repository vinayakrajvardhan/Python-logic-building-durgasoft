sentence:str = input("Enter the sentence:")

character = {}

for word in sentence:
    if word not in character:
        character[word] = 1
    else:
        character[word] = character[word] + 1

print(character)