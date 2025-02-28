def max_element(list: list):
    max = list[0]
    for ele in list:
        if ele > max:
            max = ele
    return max


list = [1, 2, 3, 4, 5]

print(max_element(list))
