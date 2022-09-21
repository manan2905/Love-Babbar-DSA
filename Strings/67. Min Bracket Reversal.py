def countRev(st):
    s = []
    c = 0
    if len(st) % 2 != 0:
        return -1
    for char in st:
        if char == "{":
            s.append(char)
        elif char == "}":
            if len(s) != 0 and s[-1] == "{":
                s.pop()
            else:
                s.append(char)
    while len(s) != 0:
        c1, c2 = s.pop(), s.pop()
        if c1 == c2:
            c += 1
        else:
            c += 2
    return c


s = input("Enter String with {} these brackets only: ")
print(countRev(s))