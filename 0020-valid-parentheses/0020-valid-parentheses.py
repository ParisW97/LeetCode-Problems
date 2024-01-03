class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        stack = []
        close_to_open = {')':'(', '}':'{', ']':'['}
        
        for c in s:
            if c in close_to_open:
                if len(stack) > 0 and stack[-1] == close_to_open[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if len(stack) > 0:
            return False
        return True