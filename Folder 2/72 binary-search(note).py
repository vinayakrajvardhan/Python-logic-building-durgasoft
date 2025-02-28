# 1. Initialize two pointers, left and right, to the start and end of the array, respectively.
# 2. Calculate the middle index mid using the formula (left + right) // 2.
# 3. Compare the middle element arr[mid] with the target value target.
# 4. If arr[mid] is equal to target, return the middle index mid.
# 5. If arr[mid] is less than target, move the left pointer to mid + 1 to search in the right half of the array.
# 6. If arr[mid] is greater than target, move the right pointer to mid - 1 to search in the left half of the array.
# 7. Repeat steps 2-6 until left is lesser than right.
# 8. If left is greater than right, it means the target value is not in the array, so return -1.

def binary_search(list: list, target_ele):
    left = 0
    right = len(list) -1
    while left <= right:
        mid = (left + right) // 2
        if list[mid] == target_ele:
            return mid
        elif list[mid] < target_ele:
            left = mid + 1
        elif list[mid] > target_ele:
            right = mid - 1

    return -1


list = [1, 2, 3, 4, 5]
target = 4
index = binary_search(list, target)
print(index)
