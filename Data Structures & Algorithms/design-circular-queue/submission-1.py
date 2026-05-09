class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None


class MyCircularQueue:

    def __init__(self, k: int):
        self.size = 0
        self.limit = k
        self.head = None
        self.curr = None

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        node = ListNode(value)
        if not self.head:
            self.head = node
        
        if not self.curr:
            self.curr = self.head
        else:
            self.curr.next = node
            self.curr = self.curr.next
        
        self.curr.next = self.head
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head = self.head.next
        self.curr.next = self.head
        self.size -= 1
        if self.size == 0:
            self.head = None
            self.curr = None
        
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.head.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.curr.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.limit


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()