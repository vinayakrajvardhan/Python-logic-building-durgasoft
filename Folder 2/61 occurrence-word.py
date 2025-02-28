s = "hello"
alp = "abcdefghijklmnopqrstuvwxyz"


for i in range(len(s)):
    for j in range(len(alp)):
        if s[i] == alp[j]:
            print(s[i],j,end=" ")
