def minSwaps(self, data):
        
        ones = sum(data)

        l, r = 0, 0
        total = 0
        

        while r < ones:
            if data[r] == 1:
                total +=1
            r += 1

        maxSum = total

        while r < len(data):
            if data[l] == 1:
                total -=1
            l += 1
            
            if data[r] == 1:
                total +=1
            r += 1
            
            maxSum = max(total,maxSum)

        return ones - maxSum 