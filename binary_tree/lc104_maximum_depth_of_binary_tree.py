from helper_func import TreeNode, list_to_tree_node

def maxDepth_bfs(root: TreeNode) -> int:
    if not root:
        return 0
    from collections import deque
    q = deque([(root, 1)])
    max_depth = 1
    while q:
        node, level = q.popleft()
        if level > max_depth:
            max_depth = level
        if node.left: 
            q.append((node.left, level + 1))
        if node.right: 
            q.append((node.right, level + 1))
    return max_depth

def maxDepth_recursive(root: TreeNode) -> int:
    if not root:
        return 0
    return 1 + max(maxDepth_recursive(root.left), maxDepth_recursive(root.right))

root = list_to_tree_node([3,9,20,None,None,15,7, 4])
print(maxDepth_bfs(root))
print(maxDepth_recursive(root))

