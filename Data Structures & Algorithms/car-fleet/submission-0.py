class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        merged = sorted(zip(position, speed))
        for p,s in merged:
            t = (target-p)/s
            while stack and stack[-1] <= t:
                stack.pop()
            stack.append(t)
        return len(stack)