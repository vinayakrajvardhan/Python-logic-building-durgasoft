letter = input("Enter the letter:")


for i in letter.split():
   if i.islower():
       print(i.upper())