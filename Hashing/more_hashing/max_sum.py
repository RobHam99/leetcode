from collections import defaultdict

def max_sum(nums):
    groups = defaultdict(list)
    
    for num in nums:
        nu = str(num)
        digit_sum = 0
        for digit in nu:
            digit_sum += int(digit)
        
        groups[digit_sum].append(num)
    ans = -1
    for digit_sum in groups:
        curr = groups[digit_sum]
        if len(curr) > 1:
            curr.sort(reverse=True) # reverse sort so we can find 2 highest nums
            ans = max(ans, curr[0] + curr[1])
            
        return ans
    

print(max_sum([53, 67, 42, 51, 80]))