x = 1000

for a in range(1, x-2):
    for b in range(a, int(500-(a/2))+1):
        c = x-a-b
        if a + b + c == 1000 and a**2 + b**2 == c**2:
            print(a*b*c)
