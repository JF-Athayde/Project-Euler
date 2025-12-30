def is_prime(x):
    if x <= 1: return False
    if x == 2: return True
    if x % 2 == 0: return False

    for i in range(3, int(x**(1/2)) + 1, 2):
        if x % i == 0:
            return False
    return True

def find_prime(n):
    if n == 1: return 2 
    
    current_number = 3
    cont = 1
    
    while cont < n:
        if is_prime(current_number):
            cont += 1
            if cont == n:
                return current_number
        
        current_number += 2
        
    return current_number

x = 10001
print(find_prime(x))