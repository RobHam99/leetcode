def reverse_string(s):
    left = 0
    right = len(s) - 1
    left_letter = ''
    while left < right:
        left_letter = s[left]
        s[left] = s[right]
        s[right] = left_letter
        left += 1
        right -= 1
    return s

input_str = ['h', 'e', 'l', 'l', 'o']
input_str2 = ['H', 'a', 'n', 'n', 'a', 'h']
print(reverse_string(input_str2))