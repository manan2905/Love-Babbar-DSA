def func(arr):
    arr.sort()
    i = 0
    j = len(arr) - 1
    perm = [0] * len(arr)
    flag = True
    k = 0
    while k != len(arr):
        if flag:
            perm[k] = arr[i]
            i += 1
            flag = False
        else:
            flag = True
            perm[k] = arr[j]
            j -= 1
        k += 1
    # print(perm)
    res = 0
    for i in range(len(perm)):
        if i == len(perm) - 1:
            res += abs(perm[i] - perm[0])
        else:
            res += abs(perm[i] - perm[i + 1])
    return res


arr = [int(i) for i in input().split()]
print(func(arr))
