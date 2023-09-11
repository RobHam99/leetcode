def check_sum(nums, target):
    left = 0
    right = len(nums) - 1
    while left < right:
        if nums[left] + nums[right] > target:
            right -= 1
            
        elif nums[left] + nums[right] < target:
            left += 1

        else:
            return True
        
    return False

nums = [1, 2, 4, 6, 8, 9, 14, 15]
target = 13

print(check_sum(nums, target))