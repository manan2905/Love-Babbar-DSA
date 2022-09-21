# User function Template for python3
import heapq


class Solution:
    def maximizeSum(self, arr, n, k):
        # Your code goes here
        heapq.heapify(arr)
        while k != 0:
            ele = heapq.heappop(arr)
            if ele < 0:
                heapq.heappush(arr, -ele)
            else:
                if k % 2 == 0:
                    heapq.heappush(arr, ele)
                    break
                else:
                    heapq.heappush(arr, -ele)
                    break
            k -= 1
        return sum(arr)


# {
# Driver Code Starts
# Initial Template for Python 3

def main():
    T = int(input())

    while (T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, k = sz[0], sz[1]
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.maximizeSum(a, n, k))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
