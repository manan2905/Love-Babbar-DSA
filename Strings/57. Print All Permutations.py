def permutations(s):
    if len(s) == 0:
        return [""]
    out = permutations(s[1:])
    final = []
    for j in range(len(out)):
        word = out[j]
        for i in range(len(word) + 1):
            final.append(word[:i] + s[0] + word[i:])
    return final


s = input("Enter String: ")
print(permutations(s))
