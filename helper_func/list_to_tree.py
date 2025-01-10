class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

def list_to_tree_node(data: list[int]) -> TreeNode:
    if not data:
        return None

    root = TreeNode(data[0])
    queue = deque([root])
    i = 1

    while queue and i < len(data):
        current = queue.popleft()

        if data[i] is not None: # add left child
            current.left = TreeNode(data[i])
            queue.append(current.left)
        i += 1

        if i< len(data) and data[i] is not None: # add right child
            current.right = TreeNode(data[i])
            queue.append(current.right)
        i += 1

    return root

def main():
    data = [5, 3, 2, 9, None, 4, 11, -3, 8, 0, None, 7, 1]

    root = list_to_tree_node(data)
    print(f'root.val: {root.val}')
    print(f'root.right.left.val: {root.right.left.val}')
    
if __name__ == '__main__':
    main()
