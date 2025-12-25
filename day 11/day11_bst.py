class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def SearchBST(root, val):
    if not root:
        return None
    if root.val == val:
        return root
    elif val < root.val:
        return SearchBST(root.left, val)
    else:
        return SearchBST(root.right, val)

# Example usage
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
result = SearchBST(root, 2)
print(result.val if result else "Not found")