from functools import cache 

def solution(nums):
    i = len(nums) - 1
    @cache
    def dp(i, nums):
        if i == 0:
            return nums[0]
        if i == 1:
            return max(nums[0], nums[1])
        
        return max(dp(i-1), nums[i] + dp(i - 2))
    
    return dp(i, nums)