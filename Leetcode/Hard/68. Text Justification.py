def fullJustify(self, words, maxWidth):
        def makeLine(sum, words):
            
            splits = len(words)-1
            gaps = maxWidth - sum
            if splits == 0:  
                ret = words[0]
                ret += " " * gaps
                print(ret)
                return ret
            else:
                leftover = gaps % splits
                spaces = gaps // splits

                ret = ""
                for s in words[:-1]:
                    ret +=s
                    ret += (" " * spaces)
                    if leftover > 0:
                        ret += " "
                        leftover -=1

                ret += words[-1]
                print(ret)
                return ret

        def makeEnd(sum, words):
            ret = ""
            for s in words:
                ret += s
                ret += " "
            
            left = maxWidth - len(ret) +1
            ret += " " * left
            print(ret)
            return ret[:-1]

        sum = 0
        currentWords = []
        ret = []
        for i, s in enumerate(words):
            if sum + len(s)+ len(currentWords) > maxWidth:
                ret.append(makeLine(sum,currentWords))
                currentWords = []
                sum = 0

            sum += len(s)
            currentWords.append(s)
            if i == len(words)-1:
                ret.append(makeEnd(sum,currentWords))

        return ret