def pseudoPalindromicPaths (self, root):
        count = [0]

        def dfs(root, num):
            if not root:
                return

            num ^= (1 << root.val)
            if root.left is None and root.right is None:
                if num & (num-1) == 0:
                    count[0] += 1
            else:
                dfs(root.left, num)
                dfs(root.right,num)

        dfs(root, 0)
        return count[0]