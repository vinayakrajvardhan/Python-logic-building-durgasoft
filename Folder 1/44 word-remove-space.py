word:str = input("Enter the word:")
for i in word:
    s = " ".join(i.split(" "))
    print(s,end=" ")