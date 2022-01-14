def max_pro_subarray(arr):
    res = max(arr)
    currMin, currMax = 1, 1
    for ele in arr:
        if ele == 0:
            currMax, currMin = 1, 1
        else:
            temp = currMax
            currMax = max(currMax * ele, currMin * ele, ele)
            currMin = min(temp * ele, currMin * ele, ele)
            res = max(currMax, currMin, res)
    return res


arr = [int(i) for i in input().split()]
print(max_pro_subarray(arr))
