# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fp = head
        for i in range(n):
            fp = fp.next
            
        if not fp:
            return head.next
        
        back = head
        while fp.next:
            back = back.next
            fp = fp.next

        back.next = back.next.next
        return head