def firstPalindrome(self, words):
        
        def isP(word):
            l, r = 0, len(word)-1
            while l < r:
                if word[l] == word[r]:
                    l += 1
                    r -=1
                    continue
                return False
            return True
        
        for word in words:
            if isP(word):
                return word
        
        return ""