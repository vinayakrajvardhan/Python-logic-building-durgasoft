
# Function to replace every element with the next greatest element
def nextGreatest(arr, n):
    for i in range(n):
        max_value = -1
        for j in range( i +1, n):
            max_value = max(max_value, arr[j])
        arr[i] = max_value

    # A utility Function that prints an array


def printArray(arr, size):
    for i in range(size):
        print(arr[i], end=" ")
    print()


# Driver program to test above function 
if __name__ == '__main__':
    arr = [16, 17, 4, 3, 5, 2]
    size = len(arr)
    nextGreatest(arr, size)
    print("The modified array is:")
    printArray(arr, size)