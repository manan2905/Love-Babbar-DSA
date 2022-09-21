def subsequences(s):
    if len(s) == 0:
        return [""]
    out = subsequences(s[1:])
    li = out.copy()
    for ele in out:
        li.append(s[0] + ele)
    return li


s = input("Enter String: ")
print(subsequences(s))
