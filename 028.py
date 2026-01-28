# top right corner = x²
# other 02 = top right corner - (x-1)
# other 03 = other 02 - (x-1)
# other 04 = other 03 - (x-1)

# (x²) + (x² - (x-1)) + (x² - 2(x-1)) + (x² - 3(x-1))
# 4x² - 6x + 6
x = 1001

pot = 1
for i in range(3, x+1, 2):
    pot += 4 * (i**2) - 6*i + 6

print(pot)