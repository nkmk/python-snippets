import calendar

print(calendar.isleap(2019))
# False

print(calendar.isleap(2020))
# True

print(calendar.isleap(1900))
# False

print(calendar.isleap(2000))
# True

print(calendar.leapdays(2019, 2030))
# 3

print(calendar.leapdays(2019, 2020))
# 0

print([y for y in range(2019, 2030) if calendar.isleap(y)])
# [2020, 2024, 2028]

print([y for y in range(2000, 2020) if calendar.isleap(y)])
# [2000, 2004, 2008, 2012, 2016]
