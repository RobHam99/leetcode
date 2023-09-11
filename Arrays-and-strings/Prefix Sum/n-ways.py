def n_ways(nums):
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[len(prefix)-1])
        
    n = 0
    for j in range(len(nums) - 1):
        if prefix[j] >= prefix[len(nums) - 1] - prefix[j]:
            n += 1
            
    return n

nums = [1, 2, 3, 4, 5]

print(n_ways(nums))