# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def inorderTraversal(node, res):
            if not node:
                return None
            
            inorderTraversal(node.left, res)
            res.append(node.val)
            inorderTraversal(node.right, res)

        res = []
        inorderTraversal(root, res)
        return res

