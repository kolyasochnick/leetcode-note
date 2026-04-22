# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        half = slow.next
        slow.next = None
        prev = None

        while half:
            nxt = half.next
            half.next = prev
            prev = half
            half = nxt
        
        reversed_half = prev
        curr = head

        while reversed_half:
            nxt1 = curr.next
            nxt2 = reversed_half.next

            curr.next = reversed_half
            reversed_half.next = nxt1

            curr = nxt1
            reversed_half = nxt2


        