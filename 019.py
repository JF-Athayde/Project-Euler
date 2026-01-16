weekday = 2 
sundays_on_first = 0

for year in range(1901, 2001):
    is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    
    if is_leap:
        months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    for m in months:
        if weekday == 0:
            sundays_on_first += 1
        
        weekday = (weekday + m) % 7

print(sundays_on_first)