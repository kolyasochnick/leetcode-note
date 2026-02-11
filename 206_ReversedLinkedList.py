# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        current = head # ListNode(1, ListNode(2, ListNode(3, None)))
        while current:
            next_node = current.next # ListNode(2, ListNode(3, None))       ListNode(3, None)                   None
            current.next = prev #      ListNode(1, None)                    ListNode(2, ListNode(1, None))      ListNode(3, NoneListNode(2, ListNode(1, None)) )
            prev = current #           ListNode(1, None)                    ListNode(2, ListNode(1, None))      ListNode(3, NoneListNode(2, ListNode(1, None)) )
            current = next_node #      ListNode(2, ListNode(3, None))       ListNode(3, None)                   None
        return prev
        