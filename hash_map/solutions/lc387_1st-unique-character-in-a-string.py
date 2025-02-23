from collections import defaultdict

def firstUniqueChar(s:str) -> int:
    hashmap = defaultdict(int)
    for char in s:
        hashmap[char] += 1
    for i, char in enumerate(s):
        if hashmap[char] == 1:
            return i
    return -1

print(firstUniqueChar("leetcode"))
print(firstUniqueChar("loveleetcode"))
print(firstUniqueChar("aabb"))
