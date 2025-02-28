list = [10,20,30,40,50,55]

sum = 0

i = 0

j = i + 1

while i != len(list)-1 :
    sum = sum + list[j] - list[i]
    i = i + 1
    j = j + 1

print(f'sum of adjacent element is:{sum}')
