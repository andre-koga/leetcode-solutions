class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        closing = {')': '(', '}': '{', ']': '['}

        stack = []
        for i in range(len(s)):
            if s[i] in closing.keys():
                if len(stack) == 0 or stack[-1] != closing[s[i]]:
                    return False
                # it matches, remove from stack
                stack.pop()
            else:
                stack.append(s[i])
    
        return stack == []