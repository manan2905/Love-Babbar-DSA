def percolateDown(arr, i):
    pi = i
    c1, c2 = 2 * pi + 1, 2 * pi + 2
    while c1 < len(arr):
        min = pi
        if arr[c1] > arr[min]:
            min = pi
        if c2 < len(arr) and arr[c2] > arr[min]:
            min = c2
        if min == pi:
            break
        arr[min], arr[pi] = arr[pi], arr[min]
        pi = min
        c1, c2 = 2 * pi + 1, 2 * pi + 2


# ignore the fact that it is a min heap consider this a simple array and use Heapify Algorithm
def minToMaxHeap(arr):
    index_last_non_leaf = len(arr) // 2 - 1
    for i in range(index_last_non_leaf, -1, -1):
        percolateDown(arr, i)


arr = [int(i) for i in input().split()]
minToMaxHeap(arr)
print(arr)
