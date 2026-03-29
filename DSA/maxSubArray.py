class Solution:
    def maxSubArray(self, nums):
        current = nums[0]
        maximum = nums[0]

        for i in nums:
            current = max(i,current + i)
            maximum = max(maximum,current)
        return maximum
    

solution = Solution()
result  = solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print(result)