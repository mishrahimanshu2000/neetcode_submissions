class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        temp = []
        n = len(position)
        for i in range(n):
            temp.append((position[i],speed[i]))
        temp.sort()
        stack = []
        for p,s in temp:
            rem = target-p
            time = rem/s
            while stack and stack[-1] <= time:
                stack.pop()
            stack.append(time)
        return len(stack)