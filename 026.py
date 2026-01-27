def period_length(denominator):
    d = abs(denominator)
    
    while d % 2 == 0:
        d //= 2
    while d % 5 == 0:
        d //= 5
        
    if d == 1:
        return 0
        
    length = 1
    remainder = 10 % d
    
    while remainder != 1:
        remainder = (remainder * 10) % d
        length += 1
        
    return length

record = (-1, -1)
for i in range(1, 1001):
    if period_length(i) > record[0]:
        record = (period_length(i), i)
print(record[1])