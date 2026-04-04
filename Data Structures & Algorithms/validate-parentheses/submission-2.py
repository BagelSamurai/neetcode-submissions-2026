class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == ')' or char == ']' or char == '}':
                if not stack:
                    return False
                prev_char = stack.pop()
                if char == ')' and prev_char == '(':
                    continue
                if char == ']' and prev_char == '[':
                    continue
                if char == '}' and prev_char == '{':
                    continue
                else:
                    return False
            elif char == '(' or char == '[' or char == '{':
                stack.append(char)
        if len(stack) == 0:
            return True
        else:
            return False