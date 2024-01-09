def dfs(root, seq):
            if not root:
                return True

            left = dfs(root.left,seq) 
            right = dfs(root.right,seq)
            
            if left and right:
                seq.append(root.val)

            return False

        seq1 = []
        seq2 = []

        dfs(root1,seq1)
        dfs(root2,seq2)
        
        return seq1 == seq2