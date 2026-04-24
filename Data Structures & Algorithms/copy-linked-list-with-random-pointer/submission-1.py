"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None        
        
        d = defaultdict(lambda: Node(0))
        d[None] = None

        curr = head
        while curr:
            d[curr].val = curr.val
            d[curr].next = d[curr.next]
            d[curr].random = d[curr.random]
            curr = curr.next
        
        return d[head]