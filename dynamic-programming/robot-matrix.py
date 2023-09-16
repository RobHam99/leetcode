from functools import cache

@cache
def dp(row, col):
    if row + col == 0:
        return 1
    
    paths = 0
    if row > 0:
        paths += dp(row - 1, col)
    if col > 0:
        paths += dp(row, col - 1)
        
    return paths

print(dp(5, 5))