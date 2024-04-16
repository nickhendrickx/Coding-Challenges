def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:

        if depth == 1:
            new_root = TreeNode(val,root)
            return new_root

        def dfs(node, dep):
            if node is None :
                return

            if dep == depth-1:
                temp_left = node.left
                temp_right = node.right
                node_left = TreeNode(val,temp_left)
                node_right = TreeNode(val,None,temp_right)
                node.left = node_left
                node.right = node_right
                return
            
            dfs(node.left, dep+1)
            dfs(node.right, dep+1)

        
        dfs(root, 1)
        return root  