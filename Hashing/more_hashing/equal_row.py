from collections import defaultdict

def equal_pairs(grid):
    def convert_to_key(arr):
        return tuple(arr)
    
    dic = defaultdict(int)
    for row in grid:
        dic[convert_to_key(row)] += 1
    
    dic2 = defaultdict(int)
    for col in range(len(grid[0])):
        current_col = []
        for row in range(len(grid)):
            current_col.append(grid[row][col])
        
        dic2[convert_to_key[current_col]] += 1
        
    ans = 0
    for arr in dic:
        ans += dic[arr] * dic2[arr]
        
    return ans