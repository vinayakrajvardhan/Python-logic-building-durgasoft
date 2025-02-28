list = [1,2,3,4,5,6,7,8]

result_even = []
result_odd = []

for i in range(len(list)):
    if list[i] % 2 == 0:
        result_even.append(list[i])
    else:
        result_odd.append(list[i])
print(f'odd number before even number :{result_odd + result_even}')
