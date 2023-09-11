from collections import defaultdict

def find_players(matches):
    loser_counts = defaultdict(int)
    seen = set()
    for w, l in matches:
        seen.add(w)
        seen.add(l)
        loser_counts[l] += 1
    
    zero_loss, one_loss = [], []
    for player in seen:
        count = loser_counts[player]
        if count == 0:
            zero_loss.append(player)
        elif count == 1:
            one_loss.append(player)
    
    return [sorted(zero_loss), sorted(one_loss)]
    
print(find_players([[2,3],[1,3],[5,4],[6,4]]))