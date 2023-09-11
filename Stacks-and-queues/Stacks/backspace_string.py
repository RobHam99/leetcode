def backspace(s, t):
    stack = []
    stack2 = []
    for c in s:
        if stack and c == '#':
            stack.pop()
        elif stack and c != '#':
            stack.append(c)
    for d in t:
        if stack2 and d == '#':
            stack2.pop()
        elif stack and d != '#':
            stack.append(d)
    return ''.join(stack) == ''.join(stack2)


print(backspace('ab#c', 'ad#c'))