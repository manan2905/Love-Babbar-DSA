# {
# Driver Code Starts

# } Driver Code Ends
def reverse(S):
    def rev(ind):
        if ind == len(S):
            return ""
        small = rev(ind + 1)
        small += S[ind]
        return small

    return rev(0)


# {
# Driver Code Starts.
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        str1 = input()
        print(reverse(str1))
# } Driver Code Ends