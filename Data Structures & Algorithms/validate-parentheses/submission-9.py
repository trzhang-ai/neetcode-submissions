class Solution:
    def isValid(self, s: str) -> bool:
        hashMap = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for char in s:
            if char in hashMap.keys():
                stack.append(char)
            elif len(stack) == 0 and char in hashMap.values():
                return False
            else:
                try:
                    if hashMap[stack[-1]] == char:
                        stack.pop(-1)
                    else:
                        stack.append(char)
                except KeyError:
                    return False
        else:
            print(stack)
            return len(stack) == 0


        