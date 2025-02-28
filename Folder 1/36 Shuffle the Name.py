name:str = input("Enter the name")

value  = []
for i in name.split(" "):
    value.append(i)

value[0],value[len(value)-1] = value[len(value)-1] ,value[0]

print(" ".join(value))


