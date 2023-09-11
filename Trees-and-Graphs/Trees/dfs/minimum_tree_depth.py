class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    

def find_min_depth(root, curr):
    if not root:
        return 0
        
    left = find_min_depth(root.left, curr)
    right = find_min_depth(root.right, curr)
    
    if not left:
        return right + 1
    elif not right:
        return left + 1
    
    return min(left, right) + 1
    