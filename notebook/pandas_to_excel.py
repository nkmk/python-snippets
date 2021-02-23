import pandas as pd

print(pd.__version__)
# 1.2.2

df = pd.DataFrame([[11, 21, 31], [12, 22, 32], [31, 32, 33]],
                  index=['one', 'two', 'three'], columns=['a', 'b', 'c'])

print(df)
#         a   b   c
# one    11  21  31
# two    12  22  32
# three  31  32  33

df.to_excel('data/dst/pandas_to_excel.xlsx', sheet_name='new_sheet_name')

df.to_excel('data/dst/pandas_to_excel_no_index_header.xlsx',
            index=False, header=False)

df2 = df[['a', 'c']]
print(df2)
#         a   c
# one    11  31
# two    12  32
# three  31  33

with pd.ExcelWriter('data/dst/pandas_to_excel_multi.xlsx') as writer:
    df.to_excel(writer, sheet_name='sheet1')
    df2.to_excel(writer, sheet_name='sheet2')

with pd.ExcelWriter('data/dst/pandas_to_excel.xlsx', mode='a') as writer:
    df.to_excel(writer, sheet_name='new_sheet1')
    df2.to_excel(writer, sheet_name='new_sheet2')
