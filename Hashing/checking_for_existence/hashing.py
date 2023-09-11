# in python a dictionary is a hash map

hash_map = {1: 2, 3: 4, 5: 6}

print(1 in hash_map)

# add to hash map

hash_map[9] = 15

print(hash_map)

# get keys
keys = hash_map.keys()
for key in keys:
    print(key)
    
values = hash_map.values()