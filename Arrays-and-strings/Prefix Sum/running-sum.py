def running_sum(nums):
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[len(prefix)-1])
        
    return prefix