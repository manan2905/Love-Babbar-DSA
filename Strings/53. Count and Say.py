def countAndSay(n):
    if n == 1:
        return "1"
    small_str = countAndSay(n - 1)
    last_char = small_str[0]
    c = 1
    final = ""
    small_str += " "
    for char in small_str[1:]:
        if char == last_char:
            c += 1
        else:
            final += str(c) + str(last_char)
            last_char = char
            c = 1

    return final


n = int(input("Enter Number: "))
print(countAndSay(n))
