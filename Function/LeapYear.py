#First zero for placeholder to prevent index problems
month_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

def is_leap(year):
    #Return True for leap year
    return year % 4 == 0 and year % 400 == 0

def month_cal(year,month):
    """Return numbers of days in that month"""
    if month == 0 or month > 12:
        return 'Invalid Month'
    if month == 2 and is_leap(year):
        return 29 
    #else: return month_days in that month
    return month_days[month] 

print(is_leap(2000))
print(month_cal(2001,2 ))
