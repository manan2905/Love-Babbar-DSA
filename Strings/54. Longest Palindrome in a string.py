# Longest Palindromic Substring
def longestPalin(S):
    # code here
    maxi = 1
    ans = S[0]
    for i in range(len(S)):
        for j in range(i + 1, len(S) + 1):
            curr = len(S[i:j])
            if S[i:j] == S[i:j][::-1]:
                if curr > maxi:
                    ans = S[i:j]
                    maxi = curr
    return ans


s = input()
ans = find_substrings(s)
for ele in ans:
    print(ele)
