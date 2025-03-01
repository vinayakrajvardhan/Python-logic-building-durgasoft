str = "Hello this is a warm day and I am solving some python questions"

d = {}

for i in str.lower():
    if i.strip() not in d:
        d[i] = 1
    else:
        d[i] = d[i] + 1

print(d)

z = max(d,key=d.get)
print(z)

# for key,value in d.items():
#     print(d.get(max(value)))