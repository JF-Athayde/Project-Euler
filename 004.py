def check_palindrome(number):
    return str(number)[::-1] == str(number)

limit = -1

for a in range(100, 999):
    for b in range(100, 999):
        new = a*b

        if check_palindrome(new) and new > limit:
            limit = new

print(limit)