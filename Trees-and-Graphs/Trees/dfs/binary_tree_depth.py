class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        

def maxDepth(root):
    if not root:
        return 0
    
    left = maxDepth(root.left)
    right = maxDepth(root.right)
    
    return max(left, right) + 1