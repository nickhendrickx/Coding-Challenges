def closestValue(self, root: Optional[TreeNode], target: float) -> int:

        out = float('inf')
        dist = float('inf')

        def dfs(node):
            if not node:
                return
            
            nonlocal out
            nonlocal dist
            new_dist = abs(node.val - target)
            if new_dist < dist:
                out = node.val
                dist = abs(node.val - target)
            
            if new_dist == dist:
                out = min(node.val, out)

            if target < node.val :
                dfs(node.left)  
            else:
                dfs(node.right)
        
        dfs(root)
        return out