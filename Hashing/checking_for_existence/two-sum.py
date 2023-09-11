def two_sum(nums, target):
    dic = {}
    for i in range(len(nums)):
        num = nums[i]
        complement = target - num
        if complement in dic:
            return [i, dic[complement]]
        
        dic[num] = i
    return [-1, -1]

nums = [1, 2, 3, 4]
target = 5