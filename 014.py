# Antes da resolução gostaria de iformar em minha língua natal que esse problema foi a primeira coisa que eu fiz no ano de 2026, OBRIGADO, vamos para a resolução
# Before I start this solve, I would like informe in my leanguage, this is the first thing of 2026, so THANKS, now come to solve

from tqdm import tqdm

def even(x):
    return x//2

def odd(x):
    return 3*x + 1

def citroen(x): # Yes I want this name
    current = x
    cont = 0

    while current > 1:
        if current in dp:
            return dp[current] + cont
        
        if current % 2 == 0:
            current = even(current)
        else:
            current = odd(current)

        cont += 1
    return cont+1
dp = {1: 1}

max_length = -1
winner_number = -1
limit = 1_000_000 

for i in tqdm(range(1, limit)):
    length = citroen(i)
    dp[i] = length
    
    if length > max_length:
        max_length = length
        winner_number = i

print(winner_number)

# WELCOME 2026
# Problem done: 1/1/2026 12:30 PM