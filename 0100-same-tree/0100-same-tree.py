# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stackp = [p]
        stackq = [q]

        while stackp and stackq:
            nodep = stackp.pop()
            nodeq = stackq.pop()

            if (not nodep and nodeq) or (nodep and not nodeq):
                return False
            if not nodep and not nodeq:
                continue

            if nodep.val == nodeq.val:
                stackp.append(nodep.left)
                stackq.append(nodeq.left)
                stackq.append(nodeq.right)
                stackp.append(nodep.right)
            else:
                return False
        return True
