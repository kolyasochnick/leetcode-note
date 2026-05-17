# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        if not root.left and not root.right:
            return True
        q = deque([root.left, root.right])
        
        while q:
            l = q.popleft()
            r = q.pop() if q else None
            print(l, r)
            if not l and not r:
                continue
            if (not l and r) or (l and not r):
                return False
            if l.val == r.val:
                q.append(r.left)
                q.append(r.right)
                q.appendleft(l.right)
                q.appendleft(l.left)
            else:
                return False
        return True