def fibonacci_mod(x):
    pot = 0 + 2 # 2 is even
    previous_numbers = [1, 2]
    current_number = -1
    while current_number < x:
        current_number = sum(previous_numbers)

        if current_number % 2 == 0:
            pot += current_number

        previous_numbers[0] = previous_numbers[1]
        previous_numbers[1] = current_number
    
    return pot

print(fibonacci_mod(int(4e6)))