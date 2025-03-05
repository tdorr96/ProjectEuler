def is_leap_year(year):

    if year % 4 == 0:
        if year % 100 == 0:
            return year % 400 == 0
        else:
            return True
    else:
        return False


def month_to_days(month, year):

    return {
        'january': 31,
        'february': 29 if is_leap_year(year) else 28,
        'march': 31,
        'april': 30,
        'may': 31,
        'june': 30,
        'july': 31,
        'august': 31,
        'september': 30,
        'october': 31,
        'november': 30,
        'december': 31
    }[month]


months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']


if __name__ == '__main__':

    # 1 jan 1900 was a monday, index 0
    days_in_1900 = sum(month_to_days(m, 1900) for m in months)
    # 365 days in 1900, which % 7 is 1, so 1 jan 1901 is a tuesday

    # for each day of the week, count how many times it fell on the first of the month during twentieth century
    first_of_month = [0 for i in range(7)]

    day_of_week_idx = 1  # start on a tuesday

    for year in range(1901, 2001):
        for month in months:
            first_of_month[day_of_week_idx] += 1
            days_in_month = month_to_days(month, year)
            weekdays_advanced = days_in_month % 7
            day_of_week_idx = (day_of_week_idx + weekdays_advanced) % 7

    # get how many sundays fell on first of month for problem answer
    print(first_of_month[6])
