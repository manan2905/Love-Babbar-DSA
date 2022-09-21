# User function template for Python 3

class Solution:
    def majorityElement(self, nums, N):
        # Your code here
        # Moore's Voting Algorithm - Majority element hona hi chahiye
        candidate = 0
        count = 0
        for ele in nums:
            if count == 0:
                candidate = ele
            if candidate == ele:
                count += 1
            else:
                count -= 1

        # found the candidate now we need to verify if this candidate is the right answer or not
        c = 0
        for ele in nums:
            if ele == candidate:
                c += 1
        if c > len(nums) // 2:
            return candidate
        return -1


# {
#  Driver Code Starts
# Initial Template for Python 3

import math

from sys import stdin


def main():
    T = int(input())
    while (T > 0):
        N = int(input())

        A = [int(x) for x in input().strip().split()]

        obj = Solution()
        print(obj.majorityElement(A, N))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends
