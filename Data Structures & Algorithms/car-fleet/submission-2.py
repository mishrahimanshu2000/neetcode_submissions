class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        temp = sorted(zip(position,speed))
        for p,s in temp:
            time = (target-p)/s
            while stack and stack[-1] <= time:
                stack.pop()
            stack.append(time)
        return len(stack)