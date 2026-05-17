def unique_permutations(s):
    if len(s) == 1:
        return s
    perms = unique_permutations(s[1:])
    char = s[0]
    result = []
    for perm in perms:
        for i in range(len(perm) + 1): 
            result.append(perm[:i] + char + perm[i:])
    return result

print(unique_permutations('abc'))
print(unique_permutations('abcdefghijklmnopqrstuvwxyz'))
