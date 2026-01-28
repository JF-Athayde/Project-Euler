def is_prime(x):
    if x <= 1:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, int(x**0.5) + 1, 2):
        if x % i == 0:
            return False
    return True


limits = 1000
best_a = best_b = best_n = 0

for a in range(-limits + 1, limits):
    for b in range(-limits, limits + 1):
        n = 0
        while True:
            value = n*n + a*n + b
            if not is_prime(value):
                break
            n += 1

        if n > best_n:
            best_n = n
            best_a = a
            best_b = b

print(best_a * best_b)
