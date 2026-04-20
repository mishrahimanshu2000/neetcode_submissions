class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            if not stack or ast > 0:
                stack.append(ast)
            else:
                pos = -ast
                while stack and stack[-1] > 0 and stack[-1] < pos:
                    stack.pop()
                if not stack or stack[-1] < 0:
                    stack.append(ast)
                elif stack[-1] == pos:
                    stack.pop()
                
        return stack