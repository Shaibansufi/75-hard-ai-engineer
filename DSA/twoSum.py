class Solution:
    def twoSum(self,nums,target):
        seen = {}
        # enumerate use karne se number ko access karsakte
        # need yani target - num
        # seen mein key -> Value pair mein num -> index hai
        
        for i,num in enumerate(nums):
            if target - num in seen:
                return [seen[target - num],i]
            seen[num] = i
solution = Solution()
print(solution.twoSum([2,5,11,15,9,7],9))