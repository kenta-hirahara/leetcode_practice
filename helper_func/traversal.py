from .treenode import TreeNode # relative imports | single dot (.) -> same directory

def preorder_recursive(node: TreeNode):
    if node:
        print(node.val, end=' ')
        preorder_recursive(node.left)
        preorder_recursive(node.right)

def inorder_recursive(node: TreeNode):
    if node:
        inorder_recursive(node.left)
        print(node.val, end=' ')
        inorder_recursive(node.right)

def postorder_recursive(node: TreeNode):
    if node:
        postorder_recursive(node.left)
        postorder_recursive(node.right)
        print(node.val, end=' ')

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

    print("pre-order recursive:")
    preorder_recursive(root)
    print("\n")

    print("in-order recursive:")
    inorder_recursive(root)
    print("\n")

    print("post-order recursive:")
    postorder_recursive(root)
    print("\n")

if __name__ == '__main__':
    main()
