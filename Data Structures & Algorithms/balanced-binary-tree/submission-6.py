class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0  # height of empty tree is 0

            left = dfs(node.left)
            if left == -1:
                return -1  # left subtree is unbalanced, exit early

            right = dfs(node.right)
            if right == -1:
                return -1  # right subtree is unbalanced, exit early

            if abs(left - right) > 1:
                return -1  # current node is unbalanced

            return 1 + max(left, right)  # return height if balanced

        return dfs(root) != -1
