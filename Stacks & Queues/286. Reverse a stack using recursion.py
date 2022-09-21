def reverseStack(s, arr):
    # [1,2,3,4,5]
    if len(s) == 0:
        return
    d = s.pop()
    arr.append(d)
    reverseStack(s, arr)


s = [int(i) for i in input().split()]
arr = []
reverseStack(s, arr)
print(arr)
