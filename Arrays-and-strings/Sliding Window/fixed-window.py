def fixed_window(nums, k):
    j = 0
    ans = 0
    curr = 0
    for i in range(len(nums)):
        curr += nums[i]
        if i - j == k:
            curr -= nums[j]
            j += 1
        ans = max(ans, curr)
    return ans

nums = [41, 2, 3, 4, 200, 8, 1, 20, 0]
k = 3

print(fixed_window(nums, k))