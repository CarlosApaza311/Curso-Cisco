def is_year_leap(year):
    a = year % 4 == 0
    b = year % 100 == 0
    c = year % 400 == 0
    return c or (not b and a)
test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr,"->",end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")
