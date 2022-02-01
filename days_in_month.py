def is_leap_year(year):
    return (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)

def days_in_month(month, year):

    if month in [9, 4, 6, 11]:
        return 30

    elif month in [1, 3, 5, 7, 8, 10, 12]:
        return 31        

    elif month == 2 and is_leap_year(year) == True:
        return 29

    elif month == 2 and is_leap_year(year) == False:
        return 28

    else:
        return None