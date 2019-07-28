import calendar
import pprint

pprint.pprint(calendar.monthcalendar(2019, 1))
# [[0, 1, 2, 3, 4, 5, 6],
#  [7, 8, 9, 10, 11, 12, 13],
#  [14, 15, 16, 17, 18, 19, 20],
#  [21, 22, 23, 24, 25, 26, 27],
#  [28, 29, 30, 31, 0, 0, 0]]

calendar.setfirstweekday(6)

pprint.pprint(calendar.monthcalendar(2019, 1))
# [[0, 0, 1, 2, 3, 4, 5],
#  [6, 7, 8, 9, 10, 11, 12],
#  [13, 14, 15, 16, 17, 18, 19],
#  [20, 21, 22, 23, 24, 25, 26],
#  [27, 28, 29, 30, 31, 0, 0]]

c = calendar.Calendar(firstweekday=0)

pprint.pprint(c.monthdayscalendar(2019, 1))
# [[0, 1, 2, 3, 4, 5, 6],
#  [7, 8, 9, 10, 11, 12, 13],
#  [14, 15, 16, 17, 18, 19, 20],
#  [21, 22, 23, 24, 25, 26, 27],
#  [28, 29, 30, 31, 0, 0, 0]]

pprint.pprint(c.yeardayscalendar(2019), depth=2)
# [[[...], [...], [...]],
#  [[...], [...], [...]],
#  [[...], [...], [...]],
#  [[...], [...], [...]]]

pprint.pprint(c.yeardayscalendar(2019, width=4), depth=2)
# [[[...], [...], [...], [...]],
#  [[...], [...], [...], [...]],
#  [[...], [...], [...], [...]]]

pprint.pprint(c.monthdays2calendar(2019, 1))
# [[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)],
#  [(7, 0), (8, 1), (9, 2), (10, 3), (11, 4), (12, 5), (13, 6)],
#  [(14, 0), (15, 1), (16, 2), (17, 3), (18, 4), (19, 5), (20, 6)],
#  [(21, 0), (22, 1), (23, 2), (24, 3), (25, 4), (26, 5), (27, 6)],
#  [(28, 0), (29, 1), (30, 2), (31, 3), (0, 4), (0, 5), (0, 6)]]

pprint.pprint(c.monthdatescalendar(2019, 1))
# [[datetime.date(2018, 12, 31),
#   datetime.date(2019, 1, 1),
#   datetime.date(2019, 1, 2),
#   datetime.date(2019, 1, 3),
#   datetime.date(2019, 1, 4),
#   datetime.date(2019, 1, 5),
#   datetime.date(2019, 1, 6)],
#  [datetime.date(2019, 1, 7),
#   datetime.date(2019, 1, 8),
#   datetime.date(2019, 1, 9),
#   datetime.date(2019, 1, 10),
#   datetime.date(2019, 1, 11),
#   datetime.date(2019, 1, 12),
#   datetime.date(2019, 1, 13)],
#  [datetime.date(2019, 1, 14),
#   datetime.date(2019, 1, 15),
#   datetime.date(2019, 1, 16),
#   datetime.date(2019, 1, 17),
#   datetime.date(2019, 1, 18),
#   datetime.date(2019, 1, 19),
#   datetime.date(2019, 1, 20)],
#  [datetime.date(2019, 1, 21),
#   datetime.date(2019, 1, 22),
#   datetime.date(2019, 1, 23),
#   datetime.date(2019, 1, 24),
#   datetime.date(2019, 1, 25),
#   datetime.date(2019, 1, 26),
#   datetime.date(2019, 1, 27)],
#  [datetime.date(2019, 1, 28),
#   datetime.date(2019, 1, 29),
#   datetime.date(2019, 1, 30),
#   datetime.date(2019, 1, 31),
#   datetime.date(2019, 2, 1),
#   datetime.date(2019, 2, 2),
#   datetime.date(2019, 2, 3)]]
