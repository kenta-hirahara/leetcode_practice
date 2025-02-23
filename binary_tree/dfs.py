from helper_func import TreeNode
from collections import deque

def dfs_iterative(root: TreeNode):
    stack = deque([root])
    while stack:
        node = stack.pop()
        if node is None:
            continue
        print(node.val, end=" ")
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


root = TreeNode(1, 
    TreeNode(2, 
        TreeNode(4), 
        TreeNode(5)
    ), 
    TreeNode(3, 
        TreeNode(6), 
        TreeNode(7)
    )
)

dfs_iterative(root)
