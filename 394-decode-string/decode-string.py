class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i]!="]":
                stack.append(s[i])
            else:
                sub = ""
                while stack[-1]!="[":
                    sub = stack.pop()+sub
                stack.pop()
                l = ""
                while stack and stack[-1].isdigit():
                    l = stack.pop()+l
                
                stack.append(int(l)*sub)
        
        return "".join(stack)