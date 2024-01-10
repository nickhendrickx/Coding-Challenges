def lowestCommonAncestor(self, root, p, q):
        lca = [0]

        def dfs(root):
            if root is None:
                return False

            else:
                
                if root == p or root == q:
                    lca[0] = root
                    return True
                
                l = dfs(root.left)
                r = dfs(root.right)

                if l and r:
                    lca[0] = root
                    return True
                
                return l or r

        dfs(root)
        return lca[0]