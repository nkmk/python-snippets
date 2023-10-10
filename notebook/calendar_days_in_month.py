import calendar

print(calendar.monthrange(2023, 1))
# (6, 31)

print(calendar.monthrange(2023, 1)[1])
# 31

print(calendar.monthrange(2023, 2)[1])
# 28

print(calendar.monthrange(2024, 2)[1])
# 29

print(calendar._monthlen(2023, 1))
# 31

print(calendar.__all__)
# ['IllegalMonthError', 'IllegalWeekdayError', 'setfirstweekday', 'firstweekday', 'isleap', 'leapdays', 'weekday', 'monthrange', 'monthcalendar', 'prmonth', 'month', 'prcal', 'calendar', 'timegm', 'month_name', 'month_abbr', 'day_name', 'day_abbr', 'Calendar', 'TextCalendar', 'HTMLCalendar', 'LocaleTextCalendar', 'LocaleHTMLCalendar', 'weekheader', 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']

print('monthrange' in calendar.__all__)
# True

print('_monthlen' in calendar.__all__)
# False
