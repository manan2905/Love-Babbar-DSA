def findDuplicates(s):
    d = {}
    ans = []
    for char in s:
        d[char] = d.get(char, 0) + 1
    for k in d:
        if d[k] > 1:
            ans.append(k)
    return ans


s = input()
print(findDuplicates(s))
