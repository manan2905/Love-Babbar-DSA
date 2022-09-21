class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        arr = []
        fact = 1
        # arr = [1,2,3,4]
        for i in range(1, n):
            # (n-1)! is completed as 4 numbers ke baad 3 ka group banega
            fact = fact * i
            arr.append(i)
        arr.append(n)
        # print(arr, fact)
        ans = ""
        # logic on 0-based indexing
        k = k - 1
        while True:
            ind = k // fact
            ans += str(arr[ind])
            arr[:] = arr[:ind] + arr[ind + 1:]
            if len(arr) == 0:
                break
            k = k % fact
            fact = fact // len(arr)
        return ans
