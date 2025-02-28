def number_occerrence(num:list[str]):
    d = {}
    for n in list:
        if n not in d:
            d[n] = 1
        else:
            d[n] = d[n] + 1
    return d

list = ['1','2','3','3']
print(number_occerrence(list))