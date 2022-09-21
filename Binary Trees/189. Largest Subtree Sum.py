# Following is the TreeNode class structure:
class BinaryTreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


def largestSubtreeSum(root):
    if root is None:
        return 0, 0
    tls, tlms = largestSubtreeSum(root.left)
    trs, trms = largestSubtreeSum(root.right)
    ts = tls + trs + root.val
    tmax = max(tlms, trms, ts)
    return ts, tmax
