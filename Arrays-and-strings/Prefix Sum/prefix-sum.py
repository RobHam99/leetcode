def prefix_sum(nums):
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[len(prefix)- 1])
    return prefix

print(prefix_sum([1, 2, 3, 4]))