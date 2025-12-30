def is_prime(x):
    if x <= 1: return False
    if x == 2: return True
    if x % 2 == 0: return False

    for i in range(3, int(x**(1/2)) + 1, 2):
        if x % i == 0:
            return False
    return True

x = 2_000_000

pot = 0

for i in range(x+1):
    if is_prime(i):
        pot += i

print(pot)