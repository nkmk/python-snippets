import pandas as pd

print(pd.__version__)
# 0.23.0

df = pd.DataFrame({'i': [0, 10, 200], 'f': [0, 0.9, 0.09],
                   's_i': ['0', '10', '200'], 's_f': ['0', '0.9', '0.09']})

print(df)
#      i     f  s_i   s_f
# 0    0  0.00    0     0
# 1   10  0.90   10   0.9
# 2  200  0.09  200  0.09

print(df.dtypes)
# i        int64
# f      float64
# s_i     object
# s_f     object
# dtype: object

print(df['i'].astype(str))
# 0      0
# 1     10
# 2    200
# Name: i, dtype: object

print(df['f'].astype(str))
# 0     0.0
# 1     0.9
# 2    0.09
# Name: f, dtype: object

print(df.astype(str))
#      i     f  s_i   s_f
# 0    0   0.0    0     0
# 1   10   0.9   10   0.9
# 2  200  0.09  200  0.09

print(df.astype(str).dtypes)
# i      object
# f      object
# s_i    object
# s_f    object
# dtype: object

print(df['i'].astype(float))
# 0      0.0
# 1     10.0
# 2    200.0
# Name: i, dtype: float64

print(df['f'].astype(int))
# 0    0
# 1    0
# 2    0
# Name: f, dtype: int64

print(df['s_i'].astype(int))
# 0      0
# 1     10
# 2    200
# Name: s_i, dtype: int64

print(df['s_i'].astype(float))
# 0      0.0
# 1     10.0
# 2    200.0
# Name: s_i, dtype: float64

print(df['s_f'].astype(float))
# 0    0.00
# 1    0.90
# 2    0.09
# Name: s_f, dtype: float64

# print(df['s_f'].astype(int))
# ValueError: invalid literal for int() with base 10: '0.1'

print(df['s_f'].astype(float).astype(int))
# 0    0
# 1    0
# 2    0
# Name: s_f, dtype: int64

df['i'] = df['i'].astype(str)
print(df)
#      i     f  s_i   s_f
# 0    0  0.00    0     0
# 1   10  0.90   10   0.9
# 2  200  0.09  200  0.09

df['f_s'] = df['f'].astype(str)
print(df)
#      i     f  s_i   s_f   f_s
# 0    0  0.00    0     0   0.0
# 1   10  0.90   10   0.9   0.9
# 2  200  0.09  200  0.09  0.09

print(df.dtypes)
# i       object
# f      float64
# s_i     object
# s_f     object
# f_s     object
# dtype: object

s_int = pd.Series([0xff, 0o77, 0b11])

print(s_int)
# 0    255
# 1     63
# 2      3
# dtype: int64

print(s_int.map(bin))
# 0    0b11111111
# 1      0b111111
# 2          0b11
# dtype: object

print(s_int.map(oct))
# 0    0o377
# 1     0o77
# 2      0o3
# dtype: object

print(s_int.map(hex))
# 0    0xff
# 1    0x3f
# 2     0x3
# dtype: object

print(s_int.map('{:b}'.format))
# 0    11111111
# 1      111111
# 2          11
# dtype: object

print(s_int.map('{:#b}'.format))
# 0    0b11111111
# 1      0b111111
# 2          0b11
# dtype: object

print(s_int.map('{:#010b}'.format))
# 0    0b11111111
# 1    0b00111111
# 2    0b00000011
# dtype: object

df_str = pd.DataFrame({'bin': ['0b01', '0b10', '0b11'],
                       'oct': ['0o07', '0o70', '0o77'],
                       'hex': ['0x0f', '0xf0', '0xff'],
                       'dec': ['1', '10', '11']})

print(df_str)
#     bin   oct   hex dec
# 0  0b01  0o07  0x0f   1
# 1  0b10  0o70  0xf0  10
# 2  0b11  0o77  0xff  11

print(df_str.dtypes)
# bin    object
# oct    object
# hex    object
# dec    object
# dtype: object

# print(df_str['bin'].astype(int))
# ValueError: invalid literal for int() with base 10: '0b01'

print(df_str['bin'].map(lambda x: int(x, 2)))
# 0    1
# 1    2
# 2    3
# Name: bin, dtype: int64

print(df_str['oct'].map(lambda x: int(x, 8)))
# 0     7
# 1    56
# 2    63
# Name: oct, dtype: int64

print(df_str['hex'].map(lambda x: int(x, 16)))
# 0     15
# 1    240
# 2    255
# Name: hex, dtype: int64

print(df_str.applymap(lambda x: int(x, 0)))
#    bin  oct  hex  dec
# 0    1    7   15    1
# 1    2   56  240   10
# 2    3   63  255   11

print(df_str['dec'].map(lambda x: int(x, 2)))
# 0    1
# 1    2
# 2    3
# Name: dec, dtype: int64

s_str_dec = pd.Series(['01', '10', '11'])

print(s_str_dec)
# 0    01
# 1    10
# 2    11
# dtype: object

print(s_str_dec.astype(int))
# 0     1
# 1    10
# 2    11
# dtype: int64

# print(s_str_dec.map(lambda x: int(x, 0)))
# ValueError: invalid literal for int() with base 0: '01'

print(df_str['oct'].map(lambda x: int(x, 8)).map(hex))
# 0     0x7
# 1    0x38
# 2    0x3f
# Name: oct, dtype: object

s_str = pd.Series(['0', '10', 'xxx'])

print(s_str)
# 0      0
# 1     10
# 2    xxx
# dtype: object

print(s_str.str.zfill(8))
# 0    00000000
# 1    00000010
# 2    00000xxx
# dtype: object

print(s_str.str.rjust(8))
# 0           0
# 1          10
# 2         xxx
# dtype: object

print(s_str.str.rjust(8, '_'))
# 0    _______0
# 1    ______10
# 2    _____xxx
# dtype: object

print(s_str.str.center(8))
# 0       0    
# 1       10   
# 2      xxx   
# dtype: object

print(s_str.str.center(8, '_'))
# 0    ___0____
# 1    ___10___
# 2    __xxx___
# dtype: object

print(s_str.str.ljust(8))
# 0    0       
# 1    10      
# 2    xxx     
# dtype: object

print(s_str.str.ljust(8, '_'))
# 0    0_______
# 1    10______
# 2    xxx_____
# dtype: object

s_num = pd.Series([0, 10, 100])

# print(s_num.str.rjust(8, '_'))
# AttributeError: Can only use .str accessor with string values, which use np.object_ dtype in pandas

print(s_num.astype(str).str.rjust(8, '_'))
# 0    _______0
# 1    ______10
# 2    _____100
# dtype: object

df = pd.DataFrame({'i': [0, 10, 100],
                   'f': [0.1234, 1.234, 12.34],
                   'round': [0.4, 0.5, 0.6]})

print(df)
#      i        f  round
# 0    0   0.1234    0.4
# 1   10   1.2340    0.5
# 2  100  12.3400    0.6

print(df.dtypes)
# i          int64
# f        float64
# round    float64
# dtype: object

print(df['i'].map('{:08}'.format))
# 0    00000000
# 1    00000010
# 2    00000100
# Name: i, dtype: object

print(df['i'].map('{:_<8}'.format))
# 0    0_______
# 1    10______
# 2    100_____
# Name: i, dtype: object

print(df['i'].map('{:x}'.format))
# 0     0
# 1     a
# 2    64
# Name: i, dtype: object

print(df['i'].map('{:#010b}'.format))
# 0    0b00000000
# 1    0b00001010
# 2    0b01100100
# Name: i, dtype: object

print(df['f'].map('{:.2f}'.format))
# 0     0.12
# 1     1.23
# 2    12.34
# Name: f, dtype: object

print(df['f'].map('{:.2g}'.format))
# 0    0.12
# 1     1.2
# 2      12
# Name: f, dtype: object

print(df['f'].map('{:.2e}'.format))
# 0    1.23e-01
# 1    1.23e+00
# 2    1.23e+01
# Name: f, dtype: object

print(df['f'].map('{:.2%}'.format))
# 0      12.34%
# 1     123.40%
# 2    1234.00%
# Name: f, dtype: object

print(df['round'].map('{:.0f}'.format))
# 0    0
# 1    0
# 2    1
# Name: round, dtype: object
