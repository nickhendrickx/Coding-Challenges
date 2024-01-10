def isSameTree(self, p, q):
    
        def dfs(p,q):
            if p is None and q is None:
                return True

            if p is None or q is None:
                return False

            elif p.val != q.val:
                return False

            else:
                return dfs(p.left,q.left) and dfs(p.right,q.right)

        return dfs(p,q)
