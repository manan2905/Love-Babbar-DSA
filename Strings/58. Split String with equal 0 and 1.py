def split_string(s):
    # given string is a binary string
    count0 = 0
    count1 = 0
    c = 0
    for char in s:
        if int(char) == 0:
            count0 += 1
        else:
            count1 += 1
        if count1 == count0:
            c += 1
    return c


s = input("Enter Binary String: ")
print(split_string(s))
