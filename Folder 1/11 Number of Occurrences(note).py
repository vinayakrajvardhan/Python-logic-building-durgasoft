def countFreq(arr, target):
    res = 0
    for i in range(len(arr)):

        # If the current element is equal to
        # target, increment the result
        if arr[i] == target:
            res += 1

    return res


arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
target = 2
print(countFreq(arr, target))