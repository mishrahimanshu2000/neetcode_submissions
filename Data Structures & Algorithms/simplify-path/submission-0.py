class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for s in path.split("/"):
            if s == '..':
                if stack:
                    stack.pop()
            elif s not in ['', '.']:
                stack.append(s)
        return "/" + "/".join(stack)