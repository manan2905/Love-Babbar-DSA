def checkPalindrome(s):
    for i in range(len(s) // 2):
        if s[i] == s[-1 - i]:
            continue
        else:
            return False
    return True


s = input()
print(checkPalindrome(s))
