class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {"]":"[", ")":"(", "}":"{"}

        for e in s:
            if e in d:
                if stack and stack[-1]==d[e]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(e)
        
        return not stack
