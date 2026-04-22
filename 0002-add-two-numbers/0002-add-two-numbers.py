# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        curr1 = l1
        curr2 = l2
        dec = 0
        res = ListNode()
        curr = res
        while curr1 or curr2:
            if curr1 and curr2:
                s = curr1.val + curr2.val + dec
            elif curr1 and not curr2:
                s = curr1.val + dec
            else:
                s = curr2.val + dec
            curr.next = ListNode(s % 10)
            dec = s // 10
            
            curr1 = curr1.next if curr1 else None
            curr2 = curr2.next if curr2 else None
            curr = curr.next
            
        if dec:
            curr.next = ListNode(dec)
        return res.next
        

            
            