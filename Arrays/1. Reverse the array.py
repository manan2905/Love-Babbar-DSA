# recursive code;
def rev_recursive(arr, s, e):
    if s >= e:
        return
    arr[s], arr[e] = arr[e], arr[s]
    rev_recursive(arr, s + 1, e - 1)


# array slicing
def one_line(arr):
    arr[:] = arr[::-1]


# conventional swapping
def rev_arr(arr):
    s = 0
    e = len(arr) - 1
    while s <= e:
        arr[s], arr[e] = arr[e], arr[s]
        s += 1
        e -= 1


arr = [int(i) for i in input("Enter the array: ").split()]
n = len(arr)
rev_arr(arr)
print(*arr)
