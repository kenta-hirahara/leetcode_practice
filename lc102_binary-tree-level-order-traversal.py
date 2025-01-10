from helper_func import TreeNode, list_to_tree_node, print_tree_level_order

def levelOrder(root: TreeNode) -> list[list[int]]:
    if not root:
        return []

    result = []
    from collections import deque
    queue = deque([root])

    while queue:
        level = []
        num_nodes_in_the_level = len(queue)
        for _ in range(num_nodes_in_the_level):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)

    return result

# Example usage:
# Constructing the binary tree [3, 9, 20, None, None, 15, 7]
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(levelOrder(root))
