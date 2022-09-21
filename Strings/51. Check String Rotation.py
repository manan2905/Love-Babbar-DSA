def checkRotation(s1, s2):
    # we need to check if s2 is a rotation of s1 or not
    for i in range(len(s1) - 1):
        if s1 == s2:
            return True
        s1 = s1[1:] + s1[0]
    return False


def checkRotationAlter(s1, s2):
    # logic is to add s1 + s1 that will have all the combinations that will be formed
    new = s1 + s1

    # sliding window
    i, j = 0, len(s2) - 1
    while j < len(new):
        if new[i:j + 1] == s2:
            return True
        i += 1
        j += 1
    return False


s1 = input()
s2 = input()
# print(checkRotation(s1, s2))
print(checkRotationAlter(s1, s2))
