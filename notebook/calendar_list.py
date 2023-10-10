import calendar
import pprint

pprint.pprint(calendar.monthcalendar(2023, 8))
# [[0, 1, 2, 3, 4, 5, 6],
#  [7, 8, 9, 10, 11, 12, 13],
#  [14, 15, 16, 17, 18, 19, 20],
#  [21, 22, 23, 24, 25, 26, 27],
#  [28, 29, 30, 31, 0, 0, 0]]

calendar.setfirstweekday(6)

pprint.pprint(calendar.monthcalendar(2023, 8))
# [[0, 0, 1, 2, 3, 4, 5],
#  [6, 7, 8, 9, 10, 11, 12],
#  [13, 14, 15, 16, 17, 18, 19],
#  [20, 21, 22, 23, 24, 25, 26],
#  [27, 28, 29, 30, 31, 0, 0]]

c = calendar.Calendar(firstweekday=6)

pprint.pprint(c.monthdayscalendar(2023, 8))
# [[0, 0, 1, 2, 3, 4, 5],
#  [6, 7, 8, 9, 10, 11, 12],
#  [13, 14, 15, 16, 17, 18, 19],
#  [20, 21, 22, 23, 24, 25, 26],
#  [27, 28, 29, 30, 31, 0, 0]]

c = calendar.Calendar()

pprint.pprint(c.monthdayscalendar(2023, 8))
# [[0, 1, 2, 3, 4, 5, 6],
#  [7, 8, 9, 10, 11, 12, 13],
#  [14, 15, 16, 17, 18, 19, 20],
#  [21, 22, 23, 24, 25, 26, 27],
#  [28, 29, 30, 31, 0, 0, 0]]

pprint.pprint(c.yeardayscalendar(2023), depth=2)
# [[[...], [...], [...]],
#  [[...], [...], [...]],
#  [[...], [...], [...]],
#  [[...], [...], [...]]]

pprint.pprint(c.yeardayscalendar(2023, width=4), depth=2)
# [[[...], [...], [...], [...]],
#  [[...], [...], [...], [...]],
#  [[...], [...], [...], [...]]]

pprint.pprint(c.monthdays2calendar(2023, 8))
# [[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)],
#  [(7, 0), (8, 1), (9, 2), (10, 3), (11, 4), (12, 5), (13, 6)],
#  [(14, 0), (15, 1), (16, 2), (17, 3), (18, 4), (19, 5), (20, 6)],
#  [(21, 0), (22, 1), (23, 2), (24, 3), (25, 4), (26, 5), (27, 6)],
#  [(28, 0), (29, 1), (30, 2), (31, 3), (0, 4), (0, 5), (0, 6)]]

pprint.pprint(c.monthdatescalendar(2023, 8))
# [[datetime.date(2023, 7, 31),
#   datetime.date(2023, 8, 1),
#   datetime.date(2023, 8, 2),
#   datetime.date(2023, 8, 3),
#   datetime.date(2023, 8, 4),
#   datetime.date(2023, 8, 5),
#   datetime.date(2023, 8, 6)],
#  [datetime.date(2023, 8, 7),
#   datetime.date(2023, 8, 8),
#   datetime.date(2023, 8, 9),
#   datetime.date(2023, 8, 10),
#   datetime.date(2023, 8, 11),
#   datetime.date(2023, 8, 12),
#   datetime.date(2023, 8, 13)],
#  [datetime.date(2023, 8, 14),
#   datetime.date(2023, 8, 15),
#   datetime.date(2023, 8, 16),
#   datetime.date(2023, 8, 17),
#   datetime.date(2023, 8, 18),
#   datetime.date(2023, 8, 19),
#   datetime.date(2023, 8, 20)],
#  [datetime.date(2023, 8, 21),
#   datetime.date(2023, 8, 22),
#   datetime.date(2023, 8, 23),
#   datetime.date(2023, 8, 24),
#   datetime.date(2023, 8, 25),
#   datetime.date(2023, 8, 26),
#   datetime.date(2023, 8, 27)],
#  [datetime.date(2023, 8, 28),
#   datetime.date(2023, 8, 29),
#   datetime.date(2023, 8, 30),
#   datetime.date(2023, 8, 31),
#   datetime.date(2023, 9, 1),
#   datetime.date(2023, 9, 2),
#   datetime.date(2023, 9, 3)]]
