def answer_query(nums, queries, limit):
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[len(prefix)- 1])
        
    ans = []
    for query in queries:
        x = query[0]
        y = query[1]
        if prefix[y] - prefix[x - 1] < limit:
            ans.append(True)
        else:
            ans.append(False)
    return ans

print(answer_query([1, 6, 3, 2, 7, 2], [[0, 3], [2, 5], [2, 4]], 13))