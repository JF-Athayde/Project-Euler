def is_prime(x):
    if x <= 1: return False
    if x == 2: return True
    if x%2 == 0: return False

    for i in range(3, int(x**1/2)+1, 2):
        if x % i == 0:
            return False
    return True

x = 600851475143
limit = int(x ** 1/2) + 1
for num in range(2, limit):
    if x%num == 0 and is_prime(num):
        print(num)
