class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_pairs = {
            '[': ']',
            '{': '}',
            '(': ')',
            ']': '[',
            '}': '{',
            ')': '('
        }
        left_parentheses = ['[', '{', '(']
        right_parenthes = [']', '}', ')']
        for char in s:
            if char in left_parentheses:
                stack.append(char)
            else:
                if len(stack) > 0:
                    if bracket_pairs[stack[-1]] == char:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        else:
            if len(stack) > 0:
                return False
            else:
                return True
        
        