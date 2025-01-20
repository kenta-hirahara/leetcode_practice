from collections import deque

def print_tree_level_order(root):
    if not root:
        return []

    result = []
    queue = deque([root])
    while queue:
        current = queue.popleft()
        if current:
            result.append(current.val)
            queue.append(current.left)
            queue.append(current.right)
        else:
            result.append(None)
        return result
