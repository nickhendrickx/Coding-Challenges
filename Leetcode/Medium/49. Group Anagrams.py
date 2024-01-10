def groupAnagrams(self, strs):
        string_map = defaultdict(list)

        for string in strs:
            chars = [0]*26

            for char in string:
                chars[ord(char) - ord('a')] += 1
            
            tup = tuple(chars)
            string_map[tup].append(string)
        
        return string_map.values()