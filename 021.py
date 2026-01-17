from tqdm import tqdm

def d(num):
    divisors = set([0])
    for i in range(1, int(num**(1/2))+1):
        if num % i == 0:
            divisors.add(i)
            divisors.add(num // i)

    divisors = list(divisors)
    divisors.remove(num)

    return sum(divisors)

x = 10000

pot = 0
for i_ in tqdm(range(1, x+1)):
    i = x+1-i_
    a = d(i)

    if i != a:
        b = d(a)

        if a <= x and b <= x:
            if b == i:
                pot += a
print(pot)