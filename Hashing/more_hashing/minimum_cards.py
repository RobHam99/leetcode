from collections import defaultdict


def minimum_cards(cards):
    groups = defaultdict(list)
    
    for i in range(len(cards)):
        groups[cards[i]].append(i)
        
    ans = float('inf')
    for key in groups:
        arr = groups[key]
        for i in range(len(arr) - 1):
            ans = min(ans, arr[i+1] - arr[i] + 1)
            
    return ans if ans < float('inf') else - 1

