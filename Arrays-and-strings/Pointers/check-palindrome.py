def pointers(string):
    left = 0
    right = len(string) - 1
    while left < right:
        if string[left] == string[right]:
            left += 1
            right -= 1
            continue
        else:
            return False
    return True

string = 'racecar'

print(pointers(string))