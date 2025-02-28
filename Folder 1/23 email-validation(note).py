import re


m = re.fullmatch("[a-z]+[0-9|_]@gmail[.]com",input("Enter email:"))
print("true" if m!=None else "false")