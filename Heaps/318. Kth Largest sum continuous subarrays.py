from typing import List

import heapq


class Solution:
    def kthLargest(self, N: int, k: int, arr: List[int]) -> int:
        # code here
        ans = []
        for i in range(N):
            curr = arr[i]
            ans.append(curr)
            for j in range(i + 1, N):
                curr += arr[j]
                ans.append(curr)

        heapq._heapify_max(ans)
        while k != 1:
            heapq._heappop_max(ans)
            k -= 1
        return heapq._heappop_max(ans)


# {
#  Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  # array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        N = int(input())

        K = int(input())

        Arr = IntArray().Input(N)

        obj = Solution()
        res = obj.kthLargest(N, K, Arr)

        print(res)

# } Driver Code Ends
