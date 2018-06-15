import pandas as pd
import numpy as np

print(pd.__version__)
# 0.23.0

print(pd.options.display.precision)
# 6

s_decimal = pd.Series([123.456, 12.3456, 1.23456, 0.123456, 0.0123456, 0.00123456])

print(s_decimal)
# 0    123.456000
# 1     12.345600
# 2      1.234560
# 3      0.123456
# 4      0.012346
# 5      0.001235
# dtype: float64

print(s_decimal[5])
# 0.00123456

pd.options.display.precision = 4

print(s_decimal)
# 0    123.4560
# 1     12.3456
# 2      1.2346
# 3      0.1235
# 4      0.0123
# 5      0.0012
# dtype: float64

pd.options.display.precision = 2

print(s_decimal)
# 0    1.23e+02
# 1    1.23e+01
# 2    1.23e+00
# 3    1.23e-01
# 4    1.23e-02
# 5    1.23e-03
# dtype: float64

print(pd.options.display.float_format)
# None

pd.options.display.float_format = '{:.2f}'.format

print(s_decimal)
# 0   123.46
# 1    12.35
# 2     1.23
# 3     0.12
# 4     0.01
# 5     0.00
# dtype: float64

pd.options.display.float_format = '{:.4g}'.format

print(s_decimal)
# 0      123.5
# 1      12.35
# 2      1.235
# 3     0.1235
# 4    0.01235
# 5   0.001235
# dtype: float64

pd.options.display.float_format = '{:.4e}'.format

print(s_decimal)
# 0   1.2346e+02
# 1   1.2346e+01
# 2   1.2346e+00
# 3   1.2346e-01
# 4   1.2346e-02
# 5   1.2346e-03
# dtype: float64

pd.options.display.float_format = '{: <10.2%}'.format

print(s_decimal)
# 0   12345.60% 
# 1   1234.56%  
# 2   123.46%   
# 3   12.35%    
# 4   1.23%     
# 5   0.12%     
# dtype: float64

df_decimal = pd.DataFrame({'s': ['0.4', '0.5', '0.6', '1.4', '1.5', '1.6'],
                           'f': [0.4, 0.5, 0.6, 1.4, 1.5, 1.6]})

pd.options.display.float_format = '{:.0f}'.format

print(df_decimal)
#      s  f
# 0  0.4  0
# 1  0.5  0
# 2  0.6  1
# 3  1.4  1
# 4  1.5  2
# 5  1.6  2

df_decimal2 = pd.DataFrame({'s': ['0.04', '0.05', '0.06', '0.14', '0.15', '0.16'],
                            'f': [0.04, 0.05, 0.06, 0.14, 0.15, 0.16]})

pd.options.display.float_format = '{:.1f}'.format

print(df_decimal2)
#       s   f
# 0  0.04 0.0
# 1  0.05 0.1
# 2  0.06 0.1
# 3  0.14 0.1
# 4  0.15 0.1
# 5  0.16 0.2

print(pd.options.display.max_rows)
# 60

df_tall = pd.DataFrame(np.arange(300).reshape((100, 3)))

pd.options.display.max_rows = 10

print(df_tall)
#       0    1    2
# 0     0    1    2
# 1     3    4    5
# 2     6    7    8
# 3     9   10   11
# 4    12   13   14
# ..  ...  ...  ...
# 95  285  286  287
# 96  288  289  290
# 97  291  292  293
# 98  294  295  296
# 99  297  298  299
# [100 rows x 3 columns]

print(df_tall.head(10))
#     0   1   2
# 0   0   1   2
# 1   3   4   5
# 2   6   7   8
# 3   9  10  11
# 4  12  13  14
# 5  15  16  17
# 6  18  19  20
# 7  21  22  23
# 8  24  25  26
# 9  27  28  29

print(df_tall.head(20))
#      0   1   2
# 0    0   1   2
# 1    3   4   5
# 2    6   7   8
# 3    9  10  11
# 4   12  13  14
# ..  ..  ..  ..
# 15  45  46  47
# 16  48  49  50
# 17  51  52  53
# 18  54  55  56
# 19  57  58  59
# [20 rows x 3 columns]

pd.options.display.max_rows = None

print(pd.options.display.max_columns)
# 20

df_wide = pd.DataFrame(np.arange(90).reshape((3, 30)))

print(df_wide)
#    0   1   2   3   4   5   6   7   8   9  ...  20  21  22  23  24  25  26  27  \
# 0   0   1   2   3   4   5   6   7   8   9 ...  20  21  22  23  24  25  26  27   
# 1  30  31  32  33  34  35  36  37  38  39 ...  50  51  52  53  54  55  56  57   
# 2  60  61  62  63  64  65  66  67  68  69 ...  80  81  82  83  84  85  86  87   
#    28  29  
# 0  28  29  
# 1  58  59  
# 2  88  89  
# [3 rows x 30 columns]

pd.options.display.max_columns = 10

print(df_wide)
#    0   1   2   3   4  ...  25  26  27  28  29
# 0   0   1   2   3   4 ...  25  26  27  28  29
# 1  30  31  32  33  34 ...  55  56  57  58  59
# 2  60  61  62  63  64 ...  85  86  87  88  89
# [3 rows x 30 columns]

pd.options.display.max_columns = None

print(df_wide)
#    0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  \
# 0   0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18   
# 1  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48   
# 2  60  61  62  63  64  65  66  67  68  69  70  71  72  73  74  75  76  77  78   
#    19  20  21  22  23  24  25  26  27  28  29  
# 0  19  20  21  22  23  24  25  26  27  28  29  
# 1  49  50  51  52  53  54  55  56  57  58  59  
# 2  79  80  81  82  83  84  85  86  87  88  89  

print(pd.options.display.show_dimensions)
# truncate

pd.options.display.max_columns = 10

print(df_wide)
#    0   1   2   3   4  ...  25  26  27  28  29
# 0   0   1   2   3   4 ...  25  26  27  28  29
# 1  30  31  32  33  34 ...  55  56  57  58  59
# 2  60  61  62  63  64 ...  85  86  87  88  89
# [3 rows x 30 columns]

df = pd.DataFrame(np.arange(12).reshape((3, 4)))
                  
print(df)
#    0  1   2   3
# 0  0  1   2   3
# 1  4  5   6   7
# 2  8  9  10  11

pd.options.display.show_dimensions = True

print(df_wide)
#    0   1   2   3   4  ...  25  26  27  28  29
# 0   0   1   2   3   4 ...  25  26  27  28  29
# 1  30  31  32  33  34 ...  55  56  57  58  59
# 2  60  61  62  63  64 ...  85  86  87  88  89
# [3 rows x 30 columns]

print(df)
#    0  1   2   3
# 0  0  1   2   3
# 1  4  5   6   7
# 2  8  9  10  11
# [3 rows x 4 columns]

pd.options.display.show_dimensions = False

print(df_wide)
#    0   1   2   3   4  ...  25  26  27  28  29
# 0   0   1   2   3   4 ...  25  26  27  28  29
# 1  30  31  32  33  34 ...  55  56  57  58  59
# 2  60  61  62  63  64 ...  85  86  87  88  89

print(df)
#    0  1   2   3
# 0  0  1   2   3
# 1  4  5   6   7
# 2  8  9  10  11

print(pd.options.display.width)
# 80

pd.options.display.max_columns = None

print(df_wide)
#    0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  \
# 0   0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18   
# 1  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48   
# 2  60  61  62  63  64  65  66  67  68  69  70  71  72  73  74  75  76  77  78   
#    19  20  21  22  23  24  25  26  27  28  29  
# 0  19  20  21  22  23  24  25  26  27  28  29  
# 1  49  50  51  52  53  54  55  56  57  58  59  
# 2  79  80  81  82  83  84  85  86  87  88  89  

pd.options.display.width = 60

print(df_wide)
#    0   1   2   3   4   5   6   7   8   9   10  11  12  13  \
# 0   0   1   2   3   4   5   6   7   8   9  10  11  12  13   
# 1  30  31  32  33  34  35  36  37  38  39  40  41  42  43   
# 2  60  61  62  63  64  65  66  67  68  69  70  71  72  73   
#    14  15  16  17  18  19  20  21  22  23  24  25  26  27  \
# 0  14  15  16  17  18  19  20  21  22  23  24  25  26  27   
# 1  44  45  46  47  48  49  50  51  52  53  54  55  56  57   
# 2  74  75  76  77  78  79  80  81  82  83  84  85  86  87   
#    28  29  
# 0  28  29  
# 1  58  59  
# 2  88  89  

pd.options.display.width = None

print(df_wide)
#    0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  \
# 0   0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18   
# 1  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48   
# 2  60  61  62  63  64  65  66  67  68  69  70  71  72  73  74  75  76  77  78   
#    19  20  21  22  23  24  25  26  27  28  29  
# 0  19  20  21  22  23  24  25  26  27  28  29  
# 1  49  50  51  52  53  54  55  56  57  58  59  
# 2  79  80  81  82  83  84  85  86  87  88  89  

print(pd.options.display.max_colwidth)
# 50

df_long_col = pd.DataFrame({'col': ['a' * 10, 'a' * 30, 'a' * 60]})

print(df_long_col)
#                                                  col
# 0                                         aaaaaaaaaa
# 1                     aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
# 2  aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa...

pd.options.display.max_colwidth = 80

print(df_long_col)
#                                                             col
# 0                                                    aaaaaaaaaa
# 1                                aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
# 2  aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

df_long_col2 = pd.DataFrame({'col1': ['a' * 10, 'a' * 30, 'a' * 60],
                             'col2': ['a' * 10, 'a' * 30, 'a' * 60]})

pd.options.display.max_colwidth = 20

print(df_long_col2)
#                   col1                 col2
# 0           aaaaaaaaaa           aaaaaaaaaa
# 1  aaaaaaaaaaaaaaaa...  aaaaaaaaaaaaaaaa...
# 2  aaaaaaaaaaaaaaaa...  aaaaaaaaaaaaaaaa...

df_long_col_header = pd.DataFrame({'a' * 60: ['a' * 10, 'a' * 30, 'a' * 60]})

pd.options.display.max_colwidth = 40

print(df_long_col_header)
#   aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
# 0                               aaaaaaaaaa                    
# 1           aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa                    
# 2  aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa...                    

print(pd.options.display.colheader_justify)
# right

print(df_long_col)
#                                        col
# 0                               aaaaaaaaaa
# 1           aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
# 2  aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa...

pd.options.display.colheader_justify = 'left'

print(df_long_col)
#   col                                     
# 0                               aaaaaaaaaa
# 1           aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
# 2  aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa...
