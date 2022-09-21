class Solution:
    def ins(self, s, d):
        if len(s) == 1:
            if d > s[0]:
                s.append(d)
            else:
                s.insert(0, d)
            return
        for i in range(len(s) - 1):
            if d < s[i]:
                s.insert(i, d)
                break
            elif s[i] < d < s[i + 1]:
                s.insert(i + 1, d)
                break
        else:
            s.append(d)

    def sorted(self, s):
        if len(s) == 1:
            return
        d = s.pop()
        self.sorted(s)
        self.ins(s, d)


# {
#  Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.sorted(arr)
        for e in range(len(arr)):
            print(arr.pop(), end=" ")
        print()

# } Driver Code Ends
