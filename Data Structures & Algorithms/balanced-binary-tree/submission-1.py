# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def getHeight(root):
            if root is None:
                return 0
            left_height = getHeight(root.left)
            right_height = getHeight(root.right)
            tree_height = 1 + max(left_height, right_height)
            return tree_height
        
        result = []
        def dfs(root):
            if root is None:
                return
            dfs(root.left)
            result.append(abs(getHeight(root.left) - getHeight(root.right)))
            dfs(root.right)
        dfs(root)
        print(result)
        if len(result) == 0:
            return True
        elif max(result) > 1:
            return False
        else:
            return True