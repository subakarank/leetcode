# https://leetcode.com/problems/validate-binary-search-tree/
'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

    The left
    subtree
    of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.

'''
from typing import Optional

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # def validate(node, low = float('-inf'), high = float('inf')):
        #     if not node: 
        #         return True
        #     if not (low < node.val < high ):
        #         return False
        #     return validate(node.left, low, node.val ) and validate(node.right, node.val, high)
        # return validate(root)
        if not root:
            return True
        stack = [(root, float('-inf'), float('inf'))]
        while stack:
            node, low, high = stack.pop()
            if not node:
                continue
            if not (low < node.val < high ):
                return False
            stack.append((node.right, node.val, high))
            stack.append((node.left, low, node.val))
        return True 
        