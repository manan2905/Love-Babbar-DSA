def naive(mat):
    # go through each end every element of first row and find if present in the subsequent rows
    ans = []
    for j in range(len(mat[0])):
        ele = mat[0][j]
        # searching / we can modify this searching to binary search if we have column wise sorted array
        for k in range(1, len(mat)):
            if ele not in mat[k]:
                break
        else:
            ans.append(ele)
    return ans


def intersection(a1, a2):
    d = {}
    ans = []
    for ele in a1:
        d[ele] = d.get(ele, 0) + 1
    for ele in a2:
        if ele in d and d[ele] > 0:
            ans.append(ele)
            d[ele] -= 1
    return ans


def common_elements_in_rows(mat):
    if len(mat) == 0:
        return
    n, m = len(mat), len(mat[0])
    for i in range(n - 1):
        li1 = mat[i]
        li2 = mat[i + 1]
        ans = intersection(li1, li2)
        mat[i + 1] = ans
    return mat[-1]


n = int(input("Enter number of rows: "))
mat = [[int(i) for i in input().split()] for j in range(n)]
print(naive(mat))
