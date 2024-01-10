def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        l = 0
        curr = 0
        res = 0

        for c in s:
            while c in chars:
                chars.remove(s[l])
                l += 1
                curr -= 1

            chars.add(c)
            curr +=1
            res = max(res, curr)

        return res