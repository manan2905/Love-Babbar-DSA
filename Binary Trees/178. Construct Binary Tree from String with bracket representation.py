class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def construct(string):
    if len(string) == 0:
        return
    root = BinaryTreeNode(int(string[0]))
    s = []
    ls = '('
    for i in range(1, len(string)):
        if len(s) == 0:
            s.append(string[i])
            flag = True
        else:
            ls += string[i]
            if string[i] == "(":
                s.append(string[i])
            elif string[i] == ")" and string[-1] == '(':
                s.pop()
            else:
                pass


