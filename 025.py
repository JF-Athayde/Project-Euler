def fibonacci(x):
    l = [0, 1]
    for _ in range(x-1):
        l[1] = l[0] + l[1]
        l[0] = l[1] - l[0]
    return l[1]

y = 1000
x = 0
while True:
    if len(str(fibonacci(x))) >= y:
        print(x)
        break

    x += 1