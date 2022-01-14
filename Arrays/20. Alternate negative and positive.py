def alternate_neg_pos(arr):
    # Using O(n) extra space
    neg_arr = []
    pos_arr = []
    for ele in arr:
        if ele < 0:
            neg_arr.append(ele)
        else:
            pos_arr.append(ele)
    i = 0
    j, k = 0, 0
    flag = True
    while i < len(arr):
        if flag:
            if j < len(neg_arr):
                arr[i] = neg_arr[j]
                j += 1
            else:
                i -= 1
            flag = False
        else:
            if k < len(pos_arr):
                arr[i] = pos_arr[k]
                k += 1
            else:
                i -= 1
            flag = True
        i += 1


def alternate_neg_pos_constantspace(arr):
    pass


arr = [int(i) for i in input().split()]
alternate_neg_pos(arr)
print(*arr)
