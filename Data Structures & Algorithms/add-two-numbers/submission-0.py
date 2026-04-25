# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode(-1)
        ans = dummy
        while l1 and l2:
            num = l1.val+l2.val+carry
            carry = num // 10
            ans.next = ListNode(num%10)
            ans = ans.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            num = l1.val+carry
            carry = num//10
            ans.next = ListNode(num%10)
            ans = ans.next
            l1 = l1.next
        while l2:
            num = l2.val+carry
            carry = num//10
            ans.next = ListNode(num%10)
            ans = ans.next
            l2 = l2.next
        
        if carry:
            ans.next = ListNode(1)
            
        return dummy.next