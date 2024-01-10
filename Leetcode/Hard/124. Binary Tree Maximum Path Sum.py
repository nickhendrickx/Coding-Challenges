def maxPathSum(self, root):
        maxSum = [float('-inf')]

        def dfs(root):
            if root is None:
                return 0

            left_sum = dfs(root.left)
            right_sum = dfs(root.right)

            total_sum = root.val + max(left_sum, right_sum, left_sum+right_sum, 0)

            maxSum[0] = max(maxSum[0], total_sum)

            return max(root.val + left_sum, root.val + right_sum, root.val)

        dfs(root)
        return maxSum[0]