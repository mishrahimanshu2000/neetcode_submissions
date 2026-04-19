class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        def get_last_two_val():
            return [stack.pop(), stack.pop()]
        
        for ch in tokens:
            match ch:
                case '+':
                    b, a = get_last_two_val()
                    stack.append(a+b)
                case '-':
                    b, a = get_last_two_val()
                    stack.append(a-b)
                case '*':
                    b, a = get_last_two_val()
                    stack.append(a*b)
                case '/':
                    b, a = get_last_two_val()
                    stack.append(int(a/b))
                case _:
                    stack.append(int(ch))
            
        return stack[-1]