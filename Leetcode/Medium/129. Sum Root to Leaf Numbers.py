def sumNumbers(self, root: Optional[TreeNode]) -> int:

        counter = [0]

        def dfs(node, num):
            if not node:
                return 

            if not node.left and not node.right:
                counter[0] += num * 10 + node.val
                return

            dfs(node.left, (num * 10) + node.val)
            dfs(node.right, (num * 10) + node.val)
            return

        dfs(root,0)

        return counter[0]