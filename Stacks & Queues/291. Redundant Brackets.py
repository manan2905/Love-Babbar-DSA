def redundantBrackets(string):
    s = []
    for char in string:
        if char == "(":
            s.append(char)
        elif char in "+-/*":
            s.append(char)
        else:
            if char == ")":
                if s[-1] == "(":
                    return True
                else:
                    while s[-1] != "(":
                        s.pop()
                    s.pop()
    return False


s = input("Enter Expression: ")
if redundantBrackets(s):
    print("Redundant!")
else:
    print("Non-Redundant!")
