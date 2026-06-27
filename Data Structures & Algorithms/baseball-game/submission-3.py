class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans = []
        i = 0
        while i < len(operations):
            if operations[i] == '+':
                if i > 1:
                    ans.append(ans[-1] + ans[-2])
            elif operations[i] == 'D':
                if i > 0:
                    ans.append(2 * ans[-1])
            elif operations[i] == 'C':
                if i > 0:
                    ans.pop()
            else:
                ans.append(int(operations[i]))
            i += 1
        return sum(ans)
        