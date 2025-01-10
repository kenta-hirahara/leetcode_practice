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

data = [5, 3, 2, 9, None, 4, 11, -3, 8, 0, None, 7, 1]

root = list_to_tree_node(data)

print(levelOrder(root))
