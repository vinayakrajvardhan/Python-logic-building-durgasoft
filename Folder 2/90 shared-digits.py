list = ['123','145','675','788']


for i in range(len(list)-1):
    s1 = list[i]
    s2 = list[i+1]
    for j in s1:
        if j in s2:
            print(f'The value {j} is present in {s2}')
