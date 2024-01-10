def maxDepth(self, root):
        
        def dfs(root):
            if root is None:
                return 0

            return 1 + max(dfs(root.left),dfs(root.right))

        return dfs(root)