x = 319e3
pot = 0

for i in range(int(x)+1):
    square = i**2
    if square % 2 != 0:
        pot += square

print(pot)