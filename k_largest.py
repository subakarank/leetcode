def common_ancestor(root, p, q):
    if not root: 
        return None
    if root.val == p.val or root.val == q.val: 
        return root
    left = common_ancestor(root.left, p, q)
    right = common_ancestor(root.right, p , q )

    if not left:
        return right
    if not right:
        return left
    return root 
