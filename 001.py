x = 1000
multiple = [3, 5]
n = len(multiple)
validators = [False] * n
vector = [0] * n
sum_vector = set()

while not all(validators):
    for i, num in enumerate(multiple):
        new = vector[i] + num
        if new < x:
            vector[i] += num
            sum_vector.add(vector[i])
        else:
            validators[i] = True

print(sum(list(sum_vector)))