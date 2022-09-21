import heapq


# T : O(nlogn)
def heapify(arr):
    new = []
    # constant time to do this
    heapq.heapify(new)

    # this loop takes logn for insertion and n for n elements
    for ele in arr:
        heapq.heappush(new, ele)
    return new


def down_heapify(arr, i):
    pi = i
    ci1, ci2 = 2 * pi + 1, 2 * pi + 2
    while ci1 < len(arr):
        if ci2 < len(arr):
            if arr[ci1] > arr[ci2] and arr[pi] > arr[ci2]:
                arr[pi], arr[ci2] = arr[ci2], arr[pi]
                pi = ci2
            elif arr[ci1] < arr[ci2] and arr[pi] > arr[ci1]:
                arr[pi], arr[ci1] = arr[ci1], arr[pi]
                pi = ci1
            else:
                break
        else:
            if arr[pi] > arr[ci1]:
                arr[pi], arr[ci1] = arr[ci1], arr[pi]
                pi = ci1
        ci1, ci2 = 2 * pi + 1, 2 * pi + 2


def heapify2(arr):
    ind_last_non_leaf = len(arr) // 2 - 1
    for i in range(ind_last_non_leaf, -1, -1):
        # now we will perform down heapify
        down_heapify(arr, i)


def upheapify(arr, i):
    ci = i
    pi = (ci - 1) // 2
    while ci > 0:
        if arr[ci] < arr[pi]:
            arr[ci], arr[pi] = arr[pi], arr[ci]
            ci = pi
            pi = (ci - 1) // 2
        else:
            break


def heapify3(arr):
    for i in range(len(arr) - 1, -1, -1):
        upheapify(arr, i)


arr = [int(i) for i in input().split()]
final_heap = heapify(arr)
print(final_heap)
heapify3(arr)
print(arr)
