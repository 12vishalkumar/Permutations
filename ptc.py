from itertools import permutations
s, n = input().split()
n = int(n)
v = list(permutations(s, n))
result = []
for i in v:
    result.append(''.join(i))
print('\n'.join(sorted(result)))