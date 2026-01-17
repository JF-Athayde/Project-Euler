def sum_digits(num):
    cont = 0
    str_num = str(num)
    for n in str_num:
        cont += int(n)
    
    return cont

def factorial(x):
    total = 1
    for i in range(1, x+1):
        total *= i
    return total

print(sum_digits(factorial(100)))
