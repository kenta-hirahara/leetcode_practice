from helper_func import TreeNode, list_to_tree_node

# bfs to scan layer by layer. return when a node has no children
def minDepth(root: TreeNode) -> int:
    if not root:
        return 0
    level = 1
    from collections import deque
    q = deque([(root, level)])
    while q:
        node, level = q.popleft()
        if not node.left and not node.right:
            return level
        if node.left:
            q.append((node.left, level + 1))
        if node.right:
            q.append((node.right, level + 1))

root = list_to_tree_node([3,9,20,None,None,15,7, 4])
print(minDepth(root))
