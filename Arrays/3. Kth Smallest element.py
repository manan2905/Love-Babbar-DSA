import heapq


def kth_smallest(arr, k):
    # minheap
    heapq.heapify(arr)
    while k != 1:
        heapq.heappop(arr)
        k -= 1
    print(heapq.heappop(arr))


def func_maxheap(arr, k):
    new = arr[:k]
    heapq._heapify_max(new)
    mh = new[0]
    for i in range(k, len(arr)):
        if arr[i] < mh:
            heapq._heapreplace_max(new, arr[i])
    print(new[0])


arr = list(int(i) for i in input("Enter Array: ").split())
k = int(input("Enter K: "))
# kth_smallest(arr, k)
func_maxheap(arr, k)
