def merge2sorted(arr1, n, arr2, m):
    i, j = 0, 0
    while i < len(arr1) and j < m:
        if arr1[i] < arr2[j]:
            i += 1
        else:
            arr1.insert(i, arr2[j])
            j += 1
    while j < m:
        arr1.append(arr2[j])
        j += 1


arr1 = [int(i) for i in input().split()]
arr2 = [int(i) for i in input().split()]
merge2sorted(arr1, len(arr1), arr2, len(arr2))
print(*arr1)
