class Solution(object):
    def isValid(self, s):
        stack = []

        for char in s:
            # Push opening brackets onto the stack
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            else:
                # If there's no opening bracket to match
                if not stack:
                    return False

                top = stack.pop()

                # Check for matching pairs
                if char == ')' and top != '(':
                    return False
                if char == '}' and top != '{':
                    return False
                if char == ']' and top != '[':
                    return False

        # Stack should be empty if all brackets are matched
        return len(stack) == 0
