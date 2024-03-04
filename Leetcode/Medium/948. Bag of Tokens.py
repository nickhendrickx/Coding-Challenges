def bagOfTokensScore(self, tokens, power):
        
        score = 0
        max_score = 0

        tokens = sorted(tokens)
        l, r = 0, len(tokens)-1

        while l <= r:
            if l <= r and power - tokens[l] >= 0:
                power -= tokens[l]
                l += 1
                score += 1
                max_score = max(score, max_score)
            
            
            elif score > 0:
                power += tokens[r]
                score -= 1
                r -= 1

            else:
                break
            
        return max_score