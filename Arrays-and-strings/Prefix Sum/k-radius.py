def k_radius(nums, k):
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[len(prefix) - 1])
    
    avgs = []
    for i in range(len(nums)):
        if i < k or len(nums) - 1 - i < k:
            avgs.append(-1)
        else:
            s = prefix[i+k+1] - prefix[i-k]
            avgs.append(s // (1 + 2*k))
    return avgs



import numpy as np

a = np.linspace(1, 20, 20)


3, 14, 19, 10
