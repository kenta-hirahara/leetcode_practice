from helper_func import list_to_tree_node

def levelOrder(data: list[int]) -> list[list[int]]:
    root = list_to_tree_node(data)
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


print(levelOrder(data))
