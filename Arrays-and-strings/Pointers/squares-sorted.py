def squares_sorted(nums):
    n = len(nums)
    squared_nums = [0] * n
    left = 0
    right = n - 1
    for i in range(n - 1, -1, -1):
        if abs(nums[left]) < abs(nums[right]):
            square = nums[right]
            right -= 1
        else:
            square = nums[left]
            left += 1
        squared_nums[i] = square**2
    return squared_nums

nums = [-5, -3, -2, -1]

print(squares_sorted(nums))