from itertools import permutations

numbers = [i for i in range(10)]

perms = [''.join(map(str, p)) for p in permutations(numbers)]
perms = list(map(int, perms))

i = int(10e5)-1
print(perms[i])
