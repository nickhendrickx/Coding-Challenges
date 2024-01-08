def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if len(matrix) == 0:
            return 0

        output = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        def dfs(r, c):
            if output[r][c] != 0: return output[r][c]

            for x,y in [[0,1],[0,-1],[1,0],[-1,0]]:
                new_r = r + x
                new_c = c + y
                if  new_r >= 0 and new_r < len(matrix) and \
                    new_c >= 0 and new_c < len(matrix[0]) and \
                    matrix[new_r][new_c] > matrix[r][c]:
                    output[r][c] = max(output[r][c], dfs(new_r,new_c))

            output[r][c] += 1 
            return output[r][c]
            
        # Main function
        row_length = len(matrix) # 1
        col_length= len(matrix[0]) # 2
        total = 0
        for r in range(row_length):
            for c in range(col_length):
                total = max (total, dfs(r,c)) #(0,0) (0,1)
        
        return total
