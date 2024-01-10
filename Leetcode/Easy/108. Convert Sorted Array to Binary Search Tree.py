def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def arrToBST(l,r):
            # base case
            if r == l-1:
                return None

            # recursion
            mid = (l + r)//2
            left = arrToBST(l, mid-1)
            right = arrToBST(mid+1, r)

            return TreeNode(nums[mid], left, right)

        # call the recursion on the whole array
        return arrToBST(0, len(nums)-1)