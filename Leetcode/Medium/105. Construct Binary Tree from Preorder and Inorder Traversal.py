def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None

        c = preorder[0]
        idx = inorder.index(c)

        preL = preorder[1:idx+1]
        preR = preorder[idx+1:]
        inL = inorder[0:idx]
        inR = inorder[idx+1:]

        root = TreeNode(c)
        root.left = self.buildTree(preL,inL)
        root.right = self.buildTree(preR,inR)

        return root
