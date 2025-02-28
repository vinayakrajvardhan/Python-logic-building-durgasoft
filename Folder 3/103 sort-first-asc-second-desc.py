L = [10,2,3,44,6,335,7,8]

n = len(L)
# print(n)
# print(L[0:n//2])

first_half =sorted(L[0:n//2])
second_half = sorted(L[n//2 :n],reverse=True)
print(first_half + second_half)

