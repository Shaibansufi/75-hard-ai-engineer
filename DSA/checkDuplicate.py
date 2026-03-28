class Solution:
    def checkDuplicate(self,nums):
        seen = {}
        for i,num in enumerate(nums):
            if num in seen:
                return True
            seen[num] = i
        return False
    
solution = Solution()
print(solution.checkDuplicate([2,5,11,15,9,7,2]))
