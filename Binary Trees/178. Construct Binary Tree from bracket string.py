class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def constructBT(string):
    if len(string) == 0:
        return None
    root = TreeNode(string[0])
    # dividing the string into left and right
    s = []
    s.append(string[1])
    ls = ""
    ind = -1
    for i in range(2, len(string)):
        char = string[i]
        ls += char
        if char == "(":
            s.append(char)
        elif char == ")" and s[-1] == "(":
            s.pop()
        if len(s) == 0:
            ind = i
            break
    if ind == len(string) - 1:
        rs = ""
    else:
        rs = string[ind + 2:len(string) - 1]
    root.left = constructBT(ls)
    root.right = constructBT(rs)
    return root
