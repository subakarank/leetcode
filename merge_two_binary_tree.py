class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def merge_tree_recursive(root1, root2):
    if not root1:
        return root2
    if not root2:
        return root1
    merge_node = TreeNode(root1.val + root2.val)
    merge_node.left = merge_tree_recursive(root1.left, root2.left)
    merge_node.right = merge_tree_recursive(root1.right, root2.right)
    return merge_node

def merge_tree(root1, root2):
    if not root1:
        return root2
    if not root2:
        return root1
    stack = [(root1, root2)]

    while stack:
        node1, node2 = stack.pop()
        if node1 and node2:
            node1.val += node2.val
            if node1.left and node2.left:
                stack.append((node1.left, node2.left))
            elif node2.left:
                node1.left = node2.left
            if node1.right and node2.right:
                stack.append((node1.right, node2.right))
            elif node2.right:
                node1.right = node2.right
        elif node2:
            node1 = node2
    return root1


