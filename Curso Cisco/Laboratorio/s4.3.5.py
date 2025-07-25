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
    else: return 30

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")
