from helper_func import TreeNode, list_to_tree_node, levelorder

def mergeTrees(root1: TreeNode, root2: TreeNode) -> TreeNode:
    if not root1 and not root2:
        return None
    root = TreeNode()
    root.val = (root1.val if root1 else 0) + (root2.val if root2 else 0)
    root.left = mergeTrees(root1.left if root1 else None, root2.left if root2 else None)
    root.right = mergeTrees(root1.right if root1 else None, root2.right if root2 else None)
    return root

root1 = list_to_tree_node([1,3,2,5])
root2 = list_to_tree_node([2,1,3, None,4, None,7])

root = mergeTrees(root1, root2)
levelorder(root)
print("None is not displayed")
