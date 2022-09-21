def nextSmaller(arr):
    s = []
    for i in range(len(arr)):
        if len(s) == 0:
            s.append((arr[i], i))
        else:
            while len(s) != 0 and arr[i] < s[-1][0]:
                d = s.pop()
                arr[d[1]] = arr[i]
            s.append((arr[i], i))
    for k in s:
        arr[k[1]] = -1


arr = [int(i) for i in input().split()]
nextSmaller(arr)
print(arr)
