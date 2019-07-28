python3 -m calendar 2019 1
#     January 2019
# Mo Tu We Th Fr Sa Su
#     1  2  3  4  5  6
#  7  8  9 10 11 12 13
# 14 15 16 17 18 19 20
# 21 22 23 24 25 26 27
# 28 29 30 31

python3 -m calendar -h
# usage: calendar.py [-h] [-w WIDTH] [-l LINES] [-s SPACING] [-m MONTHS]
#                    [-c CSS] [-L LOCALE] [-e ENCODING] [-t {text,html}]
#                    [year] [month]
# 
# positional arguments:
#   year                  year number (1-9999)
#   month                 month number (1-12, text only)
# 
# optional arguments:
#   -h, --help            show this help message and exit
#   -L LOCALE, --locale LOCALE
#                         locale to be used from month and weekday names
#   -e ENCODING, --encoding ENCODING
#                         encoding to use for output
#   -t {text,html}, --type {text,html}
#                         output type (text or html)
# 
# text only arguments:
#   -w WIDTH, --width WIDTH
#                         width of date column (default 2)
#   -l LINES, --lines LINES
#                         number of lines for each week (default 1)
#   -s SPACING, --spacing SPACING
#                         spacing between months (default 6)
#   -m MONTHS, --months MONTHS
#                         months per row (default 3)
# 
# html only arguments:
#   -c CSS, --css CSS     CSS to use for page
