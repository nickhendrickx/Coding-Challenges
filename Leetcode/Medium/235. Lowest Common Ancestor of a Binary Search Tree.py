def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        an = None

        def dfs(node):
            if node is None:
                return False
            l = dfs(node.left)
            r = dfs(node.right)
            c = node == p or node == q
            if (l and r) or (l and c) or (r and c):
                nonlocal an
                an = node
                return True

            return l or r or c

        
        dfs(root)
        return an