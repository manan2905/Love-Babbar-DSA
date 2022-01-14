import sys


# Largest sum contiguous subarray
def kadane(arr):
    max_so_far = -sys.maxsize
    max_ending_here = 0
    for i in range(len(arr)):
        max_ending_here += arr[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far


arr = [int(i) for i in input().split()]
print(kadane(arr))
