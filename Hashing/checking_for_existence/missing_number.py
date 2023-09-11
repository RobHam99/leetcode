def missing_number(nums):
    seen = set(nums)
    
    for num in range(len(nums) + 1):
        if num not in seen:
            return num
        
        
print(missing_number([3, 0, 1]))