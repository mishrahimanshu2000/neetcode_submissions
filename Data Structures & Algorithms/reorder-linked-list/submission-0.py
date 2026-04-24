# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        
        def get_mid():
            slow = head
            fast = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        
        def reverse(node):
            prev = None
            curr = node
            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next 
            return prev
        
        mid = get_mid()
        l2 = reverse(mid.next)
        mid.next = None

        curr = head
        while l2:
            l2next = l2.next
            l2.next = curr.next
            curr.next = l2
            curr = curr.next.next
            l2 = l2next