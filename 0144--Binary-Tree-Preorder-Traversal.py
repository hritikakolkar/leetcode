"""
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack=list()
        result=list()
        stack.append(root)
        while stack:
            currNode=stack.pop()
            if currNode:
                result.append(currNode.val)
                if currNode.right:
                    stack.append(currNode.right)
                if currNode.left:
                    stack.append(currNode.left)
        return result
