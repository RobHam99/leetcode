from collections import defaultdict

def check_occurences(s):
    counts = defaultdict(int)
    
    for i in range(len(s)):
        counts[s[i]] += 1
        
    frequencies = counts.values()
    print(frequencies)
    # because each frequency is the same e.g. [2, 2, 2]; we can turn the dic 
    # into a set, because each frequency is 2, the set only has one entry, 2.
    
    return len(set(frequencies)) == 1


check_occurences('abacbc')