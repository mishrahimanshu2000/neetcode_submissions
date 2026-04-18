class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for ch in s:
            if ch == ')':
                if not st or st.pop() != '(':
                    return False
            elif ch == '}':
                if not st or st.pop() != '{':
                    return False
            elif ch == ']':
                if not st or st.pop() != '[':
                    return False
            else:
                st.append(ch)
        return not st