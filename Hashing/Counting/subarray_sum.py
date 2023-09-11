from collections import defaultdict

def subarray_sum(nums, k):
    counts = defaultdict(int)
    counts[0] = 1
    ans = curr = 0
    
    for num in nums:
        curr += num
        ans += counts[curr - k]
        counts[curr] += 1
        
    return ans