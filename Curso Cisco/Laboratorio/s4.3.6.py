def is_year_leap(year):
    a = year % 4 == 0
    b = year % 100 == 0
    c = year % 400 == 0
    return c or (not b and a)

def days_in_month(year, month):
    if month in (1, 3 ,5 ,7 ,8 ,10, 12):
        return  31
    elif month == 2:
        return 29 if is_year_leap(year) else 28
    elif month in (4, 6, 9, 11):
        return 30
    else: return None

def day_of_year(year, month, day):
    if days_in_month(year,month) == None: return None
    if day-1 not in range(days_in_month(year,month)): return None
    days = 0    
    for i in range(1,month):
        days += days_in_month(year,i)
    return days + day

print(day_of_year(2000, 1, 31))