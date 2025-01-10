from helper_func import TreeNode, list_to_tree_node, print_tree_level_order

data = [5, 3, 2, 9, None, 4, 11, -3, 8, 0, None, 7, 1]

root = list_to_tree_node(data)
print(f'root.val: {root.val}')
print(f'root.right.left.val: {root.right.left.val}')
