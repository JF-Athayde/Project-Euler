def d(num):
    if num < 2: return 0
    divisors = {1}
    for i in range(2, int(num**(1/2)) + 1):
        if num % i == 0:
            divisors.add(i)
            divisors.add(num // i)
    return sum(divisors)

limit = 28123

abundant = []
for i in range(1, limit + 1):
    if d(i) > i:
        abundant.append(i)

can_be_written = [False] * (limit + 1)

for i in range(len(abundant)):
    for j in range(i, len(abundant)):
        abundant_sum = abundant[i] + abundant[j]
        if abundant_sum <= limit:
            can_be_written[abundant_sum] = True
        else:
            break

total_sum = 0
for i in range(1, limit + 1):
    if not can_be_written[i]:
        total_sum += i

print(total_sum)