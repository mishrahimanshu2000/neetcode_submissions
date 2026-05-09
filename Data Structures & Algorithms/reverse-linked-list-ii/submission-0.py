# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        
        dummy = ListNode(-1)
        dummy.next = head
        to = head
        for _ in range(1,right):
            to = to.next
        nex = to.next
        fr = dummy
        for _ in range(1,left):
            fr = fr.next
        pr = fr
        fr = fr.next
        prev = None
        curr = fr
        while curr != nex:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        pr.next = prev
        fr.next = nex
        return dummy.next