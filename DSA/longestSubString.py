class Solution:
    def longestSubString(self,s):
        seen = {}
        window = ''
        lc = 0
        for i,x in enumerate(s):
            if s[i+1] not in window:
                window += s[i+1]
                lc +=1
            else:  
                seen[lc] = window
                lc = 0
                window = window[1:]
            return max(seen.values())
        

solution = Solution()
result = solution.longestSubString("abcabcbb")
print(result)