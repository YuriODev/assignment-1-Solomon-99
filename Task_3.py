day = int(input())
month = int(input())
year = int(input())

# leap year: Every year that is exactly divisible by four is a leap year
# Except for years that are exactly divisible by 100
# Centurial years (eg 200,300,1400) are leap years if they are exactly divisible by 400

is_leap_year = False

if year % 4 == 0 or year % 400 == 0:
    is_leap_year = True

#January 1st
if day == 1 and month == 1:
    day = 31
    month = 12
    year -= 1

#March 1st and leap year
elif day == 1 and month == 3 and is_leap_year:
    day = 29
    month = 2

#March 1st and not leap year
elif day == 1 and month == 3 and not is_leap_year:
    day = 28
    month = 2

# April, June, September, November
elif day == 1 and (month == 5 or month == 7 or month == 10 or month == 12):
    day = 30
    month -= 1

elif day == 1:
    day = 31
    month -= 1

else:
    day -= 1

print(f'{day:02d}.{month:02d}.{year}')
    
