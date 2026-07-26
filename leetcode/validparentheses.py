# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

class Solution(object):
    def isValid(self, s):
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        
        stack = []

        for char in s:
            if char in pairs.values():
                stack.append(char)
            elif stack:
                if stack[-1] == pairs[char]:
                    stack.pop()
                else:
                    return False
            else:
                return False
       
        return not stack

s = "()"
print(Solution().isValid(s))