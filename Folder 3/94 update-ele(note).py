# list = [1, 2, 3, 4, 5]
# list2 = list.copy()
# i = 0
# j = i + 1
# k = i + 2
# while i in range(len(list2) - 2):
#     list2[j] = list2[i] * list2[k]
#     i = i + 1
#     j = j + 1
#     k = k + 1
# print(list)
# print(list2)
#
# for i in range(1, len(list) - 1):
#     list[i] = list[i - 1] * list[i + 1]
# print(list)


def update_array(arr):
    n = len(arr)
    new_arr = [0] * n

    # Handle edge cases for first and last elements
    new_arr[0] = arr[0] * arr[1]
    new_arr[n-1] = arr[n-2] * arr[n-1]

    # Update middle elements
    for i in range(1, n-1):
        new_arr[i] = arr[i-1] * arr[i+1]

    return new_arr

# Test the function
arr = [1, 2, 3, 4, 5]
print("Original Array:", arr)
updated_arr = update_array(arr)
print("Updated Array:", updated_arr)
