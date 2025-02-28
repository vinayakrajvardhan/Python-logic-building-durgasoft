i = int(input("Enter the value for i:"))

j = int(input("Enter the value for j:"))

k = int(input("Enter the value for k:"))

s: int = 0

while i <= j:
    s = s + i
    i = i + 1
while j != k:
    j = j - 1
    s = s + j
print(s)
