def is_nums(nums):
    ans = []
    nums = set(nums)
    for num in nums:
        if (num + 1 not in nums) and (num - 1 not in nums):
            ans.append(num)
              
    return
        