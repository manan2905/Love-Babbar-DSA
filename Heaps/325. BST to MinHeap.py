def preorder(root, arr, i):
    if root is None:
        return
    root.data = arr[i[0]]
    i[0] += 1
    preorder(root.left, arr, i)
    preorder(root.right, arr, i)


def inorder(root, arr):
    if root is None:
        return
    inorder(root.left, arr)
    arr.append(root.data)
    inorder(root.right, arr)


def bstToMinHeap(root):
    ino = []
    inorder(root, ino)
    i = [0]
    preorder(root, ino, i)
    return root
