def longest_series(s, k):
    left = 0
    curr = 0
    ans = 0
    for right in range(len(s)):
        if s[right] == '0':
            curr += 1
        while curr > k:
            if s[left] == '0':
                curr -= 1
            left += 1
        ans = max(ans, right-left+1)
    return ans
            
string = '1101100111'
flips = 1

print(longest_series(string, flips))