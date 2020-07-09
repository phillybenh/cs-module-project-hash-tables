import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
s = words.split()
cache = {}
length = len(s)
for x in range(length - 1):
    if s[x] not in cache:
        cache[s[x]] = list(s[x+1])
    
    cache[s[x]].append(s[x+1])

# TODO: construct 5 random sentences
# Your code here

print(cache)
