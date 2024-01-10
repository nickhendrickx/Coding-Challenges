def isBalanced(self, root):
        balanced = [True]

        def dfs(root):
            if root is None:
                return 0
            
            left_height = dfs(root.left)
            right_height = dfs(root.right)

            
            if abs(left_height - right_height) > 1:
                balanced[0] = False

            return max(left_height, right_height) + 1

        dfs(root)
        return balanced[0]