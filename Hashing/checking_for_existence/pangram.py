def check_pangram(s):
    seen = set(s)

    return len(seen) == 26


print(check_pangram("thequickbrownfoxjumpsoverthelazydog"))