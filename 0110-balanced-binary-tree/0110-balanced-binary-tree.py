# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        status = False
        stack = [(root, status)]
        heights = dict()

        while stack:
            node, visited = stack.pop()
            if not node:
                continue
            if visited:
                leftHight = heights.get(node.left, 0)
                rightHight = heights.get(node.right, 0)

                if abs(rightHight - leftHight) > 1:
                    return False
                heights[node] = max(leftHight, rightHight) + 1
            
            else:
                stack.append([node, True])
                stack.append([node.left, False])
                stack.append([node.right, False])
        return True