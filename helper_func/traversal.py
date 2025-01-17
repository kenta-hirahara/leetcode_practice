from treenode import TreeNode

def preorder_recursive(node: TreeNode):
    if node:
        print(node.val, end=' ')
        preorder_recursive(node.left)
        preorder_recursive(node.right)


def main():
    # height = 0
    root = TreeNode(1)

    # height = 1
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    # height = 2
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    # height = 3
    root.left.left.left = TreeNode(8)
    root.left.left.right = TreeNode(9)
    root.left.right.left = TreeNode(10)
    root.left.right.right = TreeNode(11)
    root.right.left.left = TreeNode(12)
    root.right.left.right = TreeNode(13)
    root.right.right.left = TreeNode(14)
    root.right.right.right = TreeNode(15)

    preorder_recursive(root)

if __name__ == '__main__':
    main()
    
