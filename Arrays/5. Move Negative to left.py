"""
    Time Complexity : O(n)
    Space Complexity : O(1)
"""


def move_neg_left(arr):
    # using 2 pointers
    i, j = 0, 0
    n = len(arr)
    while j < n:
        if arr[j] < 0:
            if arr[i] >= 0:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j += 1
            else:
                j += 1
        elif arr[i] < 0:
            i += 1
        else:
            j += 1


# important
def move_left_quicksort(arr):
    j = 0
    for i in range(len(arr)):
        if arr[i] < 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1


arr = list(int(i) for i in input("Enter Array: ").split())
move_left_quicksort(arr)
print(*arr)
