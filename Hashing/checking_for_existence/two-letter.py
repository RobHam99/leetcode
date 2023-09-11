def return_double(s):
    seen = set()
    for c in s:
        if c in seen:
            return c
        
        seen.add(c)
    return ' '
    
    
s = 'abcaddb'