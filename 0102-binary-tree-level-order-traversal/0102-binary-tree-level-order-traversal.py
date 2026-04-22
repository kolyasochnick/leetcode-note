# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        queue = deque([root])
        temp = deque()
        levels = [[root.val]]

        while queue:
            node = queue.popleft()
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)
            if not queue:
                if temp:
                    levels.append([x.val for x in temp])
                queue = temp
                temp = deque()

        return levels        


        
