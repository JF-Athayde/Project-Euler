import math

def divisors(n):
    cont = 0
    limit = int(math.sqrt(n))
    
    for i in range(1, limit + 1):
        if n % i == 0:
            if i * i == n:
                cont += 1
            else:
                cont += 2
    return cont

def triangle_by_i(i):
    return i*(i+1)/2

def find_triangle(x):
    i = 1
    while True:
        d = divisors(triangle_by_i(i))
        if d > x:
            return triangle_by_i(i)
        i += 1


print(find_triangle(500))
