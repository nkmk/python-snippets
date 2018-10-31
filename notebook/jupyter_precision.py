f = 123.456789

f
# 123.456789

%precision 3
# '%.3f'

f
# 123.457

print(f)
# 123.456789

%precision 0
# '%.0f'

0.4
# 0

0.5
# 0

0.6
# 1

%precision %.4e
# '%.4e'

f
# 1.2346e+02

%precision %08.2f
# '%08.2f'

f
# 00123.46

%precision
# '%r'

f
# 123.456789
