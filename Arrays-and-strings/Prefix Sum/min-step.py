def min_step(nums):
    start_value = 1
    while True:
        total = start_value
        is_valid = True
        for num in nums:
            total += num
            if total < 1:
                is_valid = False
                break
        if is_valid:
            return start_value
        else:
            start_value += 1

nums = [-3, 2, -3, 4, 2]