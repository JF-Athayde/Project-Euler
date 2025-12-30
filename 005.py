from itertools import combinations
from tqdm import tqdm
from time import time

start = time()

def good_divisor(a, limits):
    for d in range(limits[0], limits[1]+1):
        if a/d != a//d:
            return False
    return True

def product(l):
    pot = 1
    for i in l:
        pot *= i
    return pot

def set_best_limit(limits):
    l = [i for i in range(limits[0], limits[1]+1)]
    min_comb = float('inf')

    for i in range(1, len(l)+1):
        for comb in combinations(l, i):
            comb_prod = product(list(comb))
            if good_divisor(comb_prod, limits) and comb_prod < min_comb:
                min_comb = comb_prod
    
    return min_comb

limits = [1, 20]
mc = set_best_limit(limits=limits)

print(f'Possible number(time:{round(time()-start, 2)} seconds): {mc}')

for i in tqdm(range(1, mc+1)):
    if good_divisor(i, limits):
        print(f'Right number (time:{round(time()-start, 2)}):', i)
        break
