def longest_subarray(nums, k):
    left = 0
    curr = 0
    answer = 0
    for right in range(len(nums)):
        curr += nums[right]
        while curr > k:
            curr -= nums[left]
            left += 1
        answer = max(answer, right - left + 1) # update answer
    return answer

nums = [13, 1, 2, 7, 4, 2, 1, 1, 5]
k = 8

print(longest_subarray(nums, k))