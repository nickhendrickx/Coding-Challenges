def minimumLength(self, s: str) -> int:
        l, r = 0 , len(s)-1

        while l < r and s[l] == s[r]:
                c = s[l]
                
                while l <= r and s[l] == c:
                    print("l: " + str(l))
                    l +=1
                while l <= r and s[r] == c:
                    print("r: " + str(r))
                    r -= 1

        return r - l + 1