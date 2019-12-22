sentence = "This is a common interview question, find the most repeated character in this sentence."  # its ' '
from pprint import pprint

d = {}
max_val = -1
most_repeated = None
for c in sentence:  # this is O(n)
    if c not in d:  # this is O(1)
        d[c] = 0
    d[c] += 1
    if d[c] > max_val:
        max_val = d[c]
        most_repeated = c

print(f'the most repeated character is \'{most_repeated}\' at {max_val} times')
pprint(d)
