# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder):
        if len(preorder) == 0:
            return None
        root_val = preorder[0]
        ind = -1
        for i in range(1, len(preorder)):
            if preorder[i] > root_val:
                ind = i
                break
        root = TreeNode(root_val)
        # if root.right exists in the tree
        if ind > 0:
            lp, rp = preorder[1:ind], preorder[ind:]
        else:
            lp, rp = preorder[1:], []
        # print(lp,rp)
        root.left, root.right = self.bstFromPreorder(lp), self.bstFromPreorder(rp)
        return root
