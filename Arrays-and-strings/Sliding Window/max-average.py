def find_max_average(nums, k):
    j = 0
    curr = 0
    ans = 0
    for n in range(k):
        ans += nums[n] / k
    for i in range(len(nums)):
        curr += nums[i] / k
        if i - j == k - 1:
            ans = max(ans, curr)
            curr -= nums[j] / k
            j += 1
    return ans

nums = [1, 12, -5, -6, 50, 3]
k = 4

a = find_max_average(nums, k)
print(a)