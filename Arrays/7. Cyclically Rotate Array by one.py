def rotate(arr):
    # conventional
    temp = arr[-1]
    for i in range(len(arr) - 1, 0, -1):
        arr[i] = arr[i - 1]
    arr[0] = temp


def rotate_slicing(arr):
    # slicing
    arr[:] = [arr[-1]] + arr[:-1]


arr = [int(i) for i in input().split()]
rotate_slicing(arr)
print(*arr)
