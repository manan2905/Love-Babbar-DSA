def elements_more_than_nbyk(arr, k):
    d = {}
    ans = []
    for ele in arr:
        d[ele] = d.get(ele, 0) + 1
    val = len(arr) // k
    for k in d:
        if d[k] > val:
            ans.append(k)
    return ans


arr = [int(i) for i in input().split()]
k = int(input())
print(elements_more_than_nbyk(arr, k))
