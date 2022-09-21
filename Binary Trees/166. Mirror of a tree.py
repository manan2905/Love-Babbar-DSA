def mirrorBT(root):
    if root is None:
        return
    temp = root.left
    root.left = mirrorBT(root.right)
    root.right = mirrorBT(temp)
    return root
