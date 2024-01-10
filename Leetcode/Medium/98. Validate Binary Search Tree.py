def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(lo, hi, root):
            if root is None:
                return True

            return (root.val < hi 
            and root.val > lo 
            and dfs(lo,root.val,root.left) 
            and dfs(root.val,hi,root.right) )


        return dfs(float("-inf"),float("inf"),root) 