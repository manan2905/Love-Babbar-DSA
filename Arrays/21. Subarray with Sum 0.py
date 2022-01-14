"""
Logic: Agar prefix sum 2 elements par same aata hai means beech me ek aisa subaarray tha jiska sum 0 hua.
or ek subarray ka sum 0 hua tab bhi answer True/False
"""


def subarray_sum_zero(arr):
    s = set()
    curr_sum = 0
    for i in range(len(arr)):
        curr_sum += arr[i]
        if curr_sum == 0 or curr_sum in s:
            return True
        s.add(curr_sum)
    return False


arr = [int(i) for i in input().split()]
print(subarray_sum_zero(arr))
