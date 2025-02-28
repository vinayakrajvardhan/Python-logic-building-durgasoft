word:str = input("Enter the word:")

z = word.find('bomb')

if z == -1:
    print('No bomb')
else:
    print('Duck')