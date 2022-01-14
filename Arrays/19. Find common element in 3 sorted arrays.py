"""
Given arrays are sorted and we are using the merge sort approach to solve the problem:
Taking 2 arrays a a time
"""


def common_in_3(A, B, C, n1, n2, n3):
    i, j, k = 0, 0, 0
    ans = []
    final = set()
    while i < n1 and j < n2:
        if A[i] == B[j]:
            ans.append(A[i])
            i += 1
            j += 1
        elif A[i] < B[j]:
            i += 1
        else:
            j += 1
    i = 0
    while i < len(ans) and k < n3:
        if ans[i] == C[k]:
            final.add(ans[i])
            i += 1
            k += 1
        elif ans[i] < C[k]:
            i += 1
        else:
            k += 1

    return sorted(list(final))


A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
C = [int(i) for i in input().split()]
ans = common_in_3(A, B, C, len(A), len(B), len(C))
print(*ans)
