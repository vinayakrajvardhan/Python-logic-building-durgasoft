word:str = input("Enter the word:")

if  word.isdigit() and len(word) <= 5 and not word.isspace():
    print('Valid zipcode')
else:
    print('not valid zipcode')