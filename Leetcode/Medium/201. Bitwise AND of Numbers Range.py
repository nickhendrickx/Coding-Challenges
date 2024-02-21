def rangeBitwiseAnd(self, left, right):
        while left < right:
            right = right & (right - 1)

        return left & right