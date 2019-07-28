import calendar

print(calendar.monthrange(2019, 1))
# (1, 31)

print(calendar.monthrange(2019, 1)[1])
# 31

print(calendar.monthrange(2019, 2)[1])
# 28

print(calendar.monthrange(2020, 2)[1])
# 29

print(calendar.monthlen(2019, 1))
# 31

print(calendar.__all__)
# ['IllegalMonthError', 'IllegalWeekdayError', 'setfirstweekday', 'firstweekday', 'isleap', 'leapdays', 'weekday', 'monthrange', 'monthcalendar', 'prmonth', 'month', 'prcal', 'calendar', 'timegm', 'month_name', 'month_abbr', 'day_name', 'day_abbr', 'Calendar', 'TextCalendar', 'HTMLCalendar', 'LocaleTextCalendar', 'LocaleHTMLCalendar', 'weekheader']

print('monthlen' in calendar.__all__)
# False

print('monthrange' in calendar.__all__)
# True
