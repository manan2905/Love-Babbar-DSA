# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minTree(self, root):
        if root is None:
            return
        if root.left is None:
            return root.val
        return self.minTree(root.left)

    def deleteNode(self, root, key):
        # if tree is empty
        if root is None:
            return None
        if root.val == key:
            if root.left and root.right:
                rep = self.minTree(root.right)
                # print(rep)
                root.val = rep
                root.right = self.deleteNode(root.right, rep)
                return root
            if root.left:
                return root.left
            elif root.right:
                return root.right
            else:
                return None

        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root
        else:
            root.right = self.deleteNode(root.right, key)
            return root
