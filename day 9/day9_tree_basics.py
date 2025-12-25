class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)

def preorder_traversal(root):
    if not root:
        return
    print(root.val)
    preorder_traversal(root.left)
    preorder_traversal(root.right)

preorder_traversal(root)

def inorder_traversal(root):
    if not root:
        return
    inorder_traversal(root.left)
    print(root.val)
    inorder_traversal(root.right)

inorder_traversal(root)

def postorder_traversal(root):
    if not root:
        return
    postorder_traversal(root.left)
    postorder_traversal(root.right)
    print(root.val)

postorder_traversal(root)