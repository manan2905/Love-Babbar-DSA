# User function Template for python3


def find(arr, n, x):
    # code here
    def first(arr, x):
        s = 0
        e = len(arr) - 1
        ans = -1
        while s <= e:
            mid = (s + e) // 2
            if arr[mid] == x:
                ans = mid
                e = mid - 1
            elif arr[mid] < x:
                s = mid + 1
            else:
                e = mid - 1
        return ans

    def last(arr, x):
        s = 0
        e = len(arr) - 1
        ans = -1
        while s <= e:
            mid = (s + e) // 2
            if arr[mid] == x:
                ans = mid
                s = mid + 1
            elif arr[mid] < x:
                s = mid + 1
            else:
                e = mid - 1
        return ans

    return [first(arr, x), last(arr, x)]


# {
#  Driver Code Starts
t = int(input())
for _ in range(0, t):
    l = list(map(int, input().split()))
    n = l[0]
    x = l[1]
    arr = list(map(int, input().split()))
    ans = find(arr, n, x)
    print(*ans)
# } Driver Code Ends