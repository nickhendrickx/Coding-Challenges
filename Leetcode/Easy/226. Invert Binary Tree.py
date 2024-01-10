def invertTree(self, root):
        
        def dfs(root):
            if root is None:
                return

            else:
                root.left, root.right = root.right, root.left
                dfs(root.left)
                dfs(root.right)

        dfs(root)
        return root
