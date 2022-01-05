def sort012(arr, n):
    cnt0 = 0
    cnt1 = 0
    cnt2 = 0
    for i in range(n):
        if arr[i] == 0:
            cnt0 += 1
        elif arr[i] == 1:
            cnt1 += 1
        else:
            cnt2 += 1
    i = 0
    while cnt0 != 0:
        arr[i] = 0
        cnt0 -= 1
        i += 1
    while cnt1 != 0:
        arr[i] = 1
        cnt1 -= 1
        i += 1
    while cnt2 != 0:
        arr[i] = 2
        cnt2 -= 1
        i += 1


arr = [int(i) for i in input().split()]
sort012(arr, len(arr))
print(*arr)
