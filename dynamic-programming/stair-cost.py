# dp[i] = min(dp(i-1) + cost[i-1], dp(i-2) + cost[i-2])
# base cases: dp(0)=dp(1)=0

def solution(cost):
    i = len(cost)
    def dp(i):
        if i == 0 or i == 1:
            return 0
        
        return min(dp(i-1) + cost[i-1], dp(i-2) + cost[i-2])
    
    result = dp(i)
    return result

cost = [1, 2, 3, 4]

print(solution(cost))