num = 123456
a = []

while num!=0:
    d = num % 10
    if d % 2 == 0:
      a.append(d +1)
    else:
        a.append(d)
    num = num//10



for i in a[::-1]:
    print(i,end=" ")

