import sys


# Linear search
def max_min(arr):
    mini = sys.maxsize
    maxi = -sys.maxsize
    for ele in arr:
        if mini > ele:
            mini = ele
        if maxi < ele:
            maxi = ele
    print(mini, maxi)


arr = [int(i) for i in input().split()]
max_min(arr)
