'''
Given the root node of a binary search tree and two integers low and high, 
return the sum of values of all nodes with a value in the inclusive range [low, high].
'''
from queue import Full
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def range_sum_recursive(root: Optional[TreeNode], low: int, high: int):

    def dfs(root):
        if root is None:
            return 0 
        if root.val < low:
            return dfs(root.right)
        elif root.val > high:
            return dfs(root.left)
        else: 
            return root.val + dfs(root.left) + dfs(root.right)
    return dfs(root)
 
root = [10,5,15,3,7, None,18]
low = 7
high = 15

print(range_sum_recursive(root, low, high))

root = [18,9,27,6,15,24,30,3, None, 12, None, 21]
low = 18
high = 24

def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
    if root is None:
        return 0
    stack = [root]
    range_sum = 0
    while stack: 
        node = stack.pop()
        if not node: 
            continue
        if  node.val < low:
            stack.append(node.right)
        elif node.val > high:
            stack.append(node.left)
        else: 
            range_sum += node.val
            stack.append(node.left)
            stack.append(node.right)
    return range_sum
    

