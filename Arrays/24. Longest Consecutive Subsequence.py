"""
Consecutive means - duplicates ho bhi toinclude nahi karne so this will work for both
"""
import heapq


# O(n) - approaches --- using hashing
def longest_consecutive_subsequence_length(arr):
    s = set(arr)
    max_count = -1
    for i in range(len(arr)):
        ele = arr[i]
        count = 1
        if ele - 1 not in s:
            while ele + 1 in s:
                ele += 1
                count += 1
            if max_count < count:
                max_count = count
    return max_count


def longest_consecutive_subsequence_array(arr):
    s = set(arr)
    max_count = -1
    final = []
    for i in range(len(arr)):
        ele = arr[i]
        ans = []
        count = 1
        if ele - 1 not in s:
            ans.append(ele)
            while ele + 1 in s:
                ele += 1
                ans.append(ele)
                count += 1
            if max_count < count:
                max_count = count
                final = ans.copy()
    return final


# O(nlogn) - using sorting
def longest_consecutive_subsequence_sorting(arr):
    n = len(arr)
    arr.sort()
    new_arr = [arr[0]]
    for i in range(1, n):
        if new_arr[-1] != arr[i]:
            new_arr.append(arr[i])
    maxc = 0
    count = 1
    for i in range(len(new_arr) - 1):
        if new_arr[i] + 1 == new_arr[i + 1]:
            count += 1
        else:
            maxc = max(maxc, count)
            count = 1
    maxc = max(maxc, count)
    return maxc


arr = [int(i) for i in input().split()]
print("Length of SubSequence: ", longest_consecutive_subsequence_length(arr))
print("Longest Consecutive SubSequence is: ", *longest_consecutive_subsequence_array(arr))
