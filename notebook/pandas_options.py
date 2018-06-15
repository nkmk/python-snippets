import pandas as pd
import pprint

print(pd.__version__)
# 0.23.0

print(pd.options.display.max_rows)
# 60

pd.options.display.max_rows = 100

print(pd.options.display.max_rows)
# 100

print(dir(pd.options))
# ['compute', 'display', 'html', 'io', 'mode', 'plotting']

pprint.pprint(dir(pd.options.display))
# ['chop_threshold',
#  'colheader_justify',
#  'column_space',
#  'date_dayfirst',
#  'date_yearfirst',
#  'encoding',
#  'expand_frame_repr',
#  'float_format',
#  'html',
#  'large_repr',
#  'latex',
#  'max_categories',
#  'max_columns',
#  'max_colwidth',
#  'max_info_columns',
#  'max_info_rows',
#  'max_rows',
#  'max_seq_items',
#  'memory_usage',
#  'multi_sparse',
#  'notebook_repr_html',
#  'pprint_nest_depth',
#  'precision',
#  'show_dimensions',
#  'unicode',
#  'width']

pd.describe_option()
# compute.use_bottleneck : bool
#     Use the bottleneck library to accelerate if it is installed,
#     the default is True
#     Valid values: False,True
#     [default: True] [currently: True]
# compute.use_numexpr : bool
#     Use the numexpr library to accelerate computation if it is installed,
#     the default is True
#     Valid values: False,True
#     [default: True] [currently: True]
# display.chop_threshold : float or None
#     if set to a float value, all float values smaller then the given threshold
#     will be displayed as exactly 0 by repr and friends.
#     [default: None] [currently: None]
# display.colheader_justify : 'left'/'right'
#     Controls the justification of column headers. used by DataFrameFormatter.
#     [default: right] [currently: right]
# display.column_space No description available.
#     [default: 12] [currently: 12]
# display.date_dayfirst : boolean
#     When True, prints and parses dates with the day first, eg 20/01/2005
#     [default: False] [currently: False]
# display.date_yearfirst : boolean
#     When True, prints and parses dates with the year first, eg 2005/01/20
#     [default: False] [currently: False]
# display.encoding : str/unicode
#     Defaults to the detected encoding of the console.
#     Specifies the encoding to be used for strings returned by to_string,
#     these are generally strings meant to be displayed on the console.
#     [default: UTF-8] [currently: UTF-8]
# display.expand_frame_repr : boolean
#     Whether to print out the full DataFrame repr for wide DataFrames across
#     multiple lines, `max_columns` is still respected, but the output will
#     wrap-around across multiple "pages" if its width exceeds `display.width`.
#     [default: True] [currently: True]
# display.float_format : callable
#     The callable should accept a floating point number and return
#     a string with the desired format of the number. This is used
#     in some places like SeriesFormatter.
#     See formats.format.EngFormatter for an example.
#     [default: None] [currently: None]
# display.html.border : int
#     A ``border=value`` attribute is inserted in the ``<table>`` tag
#     for the DataFrame HTML repr.
#     [default: 1] [currently: 1]
# display.html.table_schema : boolean
#     Whether to publish a Table Schema representation for frontends
#     that support it.
#     (default: False)
#     [default: False] [currently: False]
# display.html.use_mathjax : boolean
#     When True, Jupyter notebook will process table contents using MathJax,
#     rendering mathematical expressions enclosed by the dollar symbol.
#     (default: True)
#     [default: True] [currently: True]
# display.large_repr : 'truncate'/'info'
#     For DataFrames exceeding max_rows/max_cols, the repr (and HTML repr) can
#     show a truncated table (the default from 0.13), or switch to the view from
#     df.info() (the behaviour in earlier versions of pandas).
#     [default: truncate] [currently: truncate]
# display.latex.escape : bool
#     This specifies if the to_latex method of a Dataframe uses escapes special
#     characters.
#     Valid values: False,True
#     [default: True] [currently: True]
# display.latex.longtable :bool
#     This specifies if the to_latex method of a Dataframe uses the longtable
#     format.
#     Valid values: False,True
#     [default: False] [currently: False]
# display.latex.multicolumn : bool
#     This specifies if the to_latex method of a Dataframe uses multicolumns
#     to pretty-print MultiIndex columns.
#     Valid values: False,True
#     [default: True] [currently: True]
# display.latex.multicolumn_format : bool
#     This specifies if the to_latex method of a Dataframe uses multicolumns
#     to pretty-print MultiIndex columns.
#     Valid values: False,True
#     [default: l] [currently: l]
# display.latex.multirow : bool
#     This specifies if the to_latex method of a Dataframe uses multirows
#     to pretty-print MultiIndex rows.
#     Valid values: False,True
#     [default: False] [currently: False]
# display.latex.repr : boolean
#     Whether to produce a latex DataFrame representation for jupyter
#     environments that support it.
#     (default: False)
#     [default: False] [currently: False]
# display.max_categories : int
#     This sets the maximum number of categories pandas should output when
#     printing out a `Categorical` or a Series of dtype "category".
#     [default: 8] [currently: 8]
# display.max_columns : int
#     If max_cols is exceeded, switch to truncate view. Depending on
#     `large_repr`, objects are either centrally truncated or printed as
#     a summary view. 'None' value means unlimited.
#     In case python/IPython is running in a terminal and `large_repr`
#     equals 'truncate' this can be set to 0 and pandas will auto-detect
#     the width of the terminal and print a truncated object which fits
#     the screen width. The IPython notebook, IPython qtconsole, or IDLE
#     do not run in a terminal and hence it is not possible to do
#     correct auto-detection.
#     [default: 20] [currently: 20]
# display.max_colwidth : int
#     The maximum width in characters of a column in the repr of
#     a pandas data structure. When the column overflows, a "..."
#     placeholder is embedded in the output.
#     [default: 50] [currently: 50]
# display.max_info_columns : int
#     max_info_columns is used in DataFrame.info method to decide if
#     per column information will be printed.
#     [default: 100] [currently: 100]
# display.max_info_rows : int or None
#     df.info() will usually show null-counts for each column.
#     For large frames this can be quite slow. max_info_rows and max_info_cols
#     limit this null check only to frames with smaller dimensions than
#     specified.
#     [default: 1690785] [currently: 1690785]
# display.max_rows : int
#     If max_rows is exceeded, switch to truncate view. Depending on
#     `large_repr`, objects are either centrally truncated or printed as
#     a summary view. 'None' value means unlimited.
#     In case python/IPython is running in a terminal and `large_repr`
#     equals 'truncate' this can be set to 0 and pandas will auto-detect
#     the height of the terminal and print a truncated object which fits
#     the screen height. The IPython notebook, IPython qtconsole, or
#     IDLE do not run in a terminal and hence it is not possible to do
#     correct auto-detection.
#     [default: 60] [currently: 100]
# display.max_seq_items : int or None
#     when pretty-printing a long sequence, no more then `max_seq_items`
#     will be printed. If items are omitted, they will be denoted by the
#     addition of "..." to the resulting string.
#     If set to None, the number of items to be printed is unlimited.
#     [default: 100] [currently: 100]
# display.memory_usage : bool, string or None
#     This specifies if the memory usage of a DataFrame should be displayed when
#     df.info() is called. Valid values True,False,'deep'
#     [default: True] [currently: True]
# display.multi_sparse : boolean
#     "sparsify" MultiIndex display (don't display repeated
#     elements in outer levels within groups)
#     [default: True] [currently: True]
# display.notebook_repr_html : boolean
#     When True, IPython notebook will use html representation for
#     pandas objects (if it is available).
#     [default: True] [currently: True]
# display.pprint_nest_depth : int
#     Controls the number of nested levels to process when pretty-printing
#     [default: 3] [currently: 3]
# display.precision : int
#     Floating point output precision (number of significant digits). This is
#     only a suggestion
#     [default: 6] [currently: 6]
# display.show_dimensions : boolean or 'truncate'
#     Whether to print out dimensions at the end of DataFrame repr.
#     If 'truncate' is specified, only print out the dimensions if the
#     frame is truncated (e.g. not display all rows and/or columns)
#     [default: truncate] [currently: truncate]
# display.unicode.ambiguous_as_wide : boolean
#     Whether to use the Unicode East Asian Width to calculate the display text
#     width.
#     Enabling this may affect to the performance (default: False)
#     [default: False] [currently: False]
# display.unicode.east_asian_width : boolean
#     Whether to use the Unicode East Asian Width to calculate the display text
#     width.
#     Enabling this may affect to the performance (default: False)
#     [default: False] [currently: False]
# display.width : int
#     Width of the display in characters. In case python/IPython is running in
#     a terminal this can be set to None and pandas will correctly auto-detect
#     the width.
#     Note that the IPython notebook, IPython qtconsole, or IDLE do not run in a
#     terminal and hence it is not possible to correctly detect the width.
#     [default: 80] [currently: 80]
# html.border : int
#     A ``border=value`` attribute is inserted in the ``<table>`` tag
#     for the DataFrame HTML repr.
#     [default: 1] [currently: 1]
#     (Deprecated, use `display.html.border` instead.)
# io.excel.xls.writer : string
#     The default Excel writer engine for 'xls' files. Available options:
#     auto, xlwt.
#     [default: auto] [currently: auto]
# io.excel.xlsm.writer : string
#     The default Excel writer engine for 'xlsm' files. Available options:
#     auto, openpyxl.
#     [default: auto] [currently: auto]
# io.excel.xlsx.writer : string
#     The default Excel writer engine for 'xlsx' files. Available options:
#     auto, openpyxl, xlsxwriter.
#     [default: auto] [currently: auto]
# io.hdf.default_format : format
#     default format writing format, if None, then
#     put will default to 'fixed' and append will default to 'table'
#     [default: None] [currently: None]
# io.hdf.dropna_table : boolean
#     drop ALL nan rows when appending to a table
#     [default: False] [currently: False]
# io.parquet.engine : string
#     The default parquet reader/writer engine. Available options:
#     'auto', 'pyarrow', 'fastparquet', the default is 'auto'
#     [default: auto] [currently: auto]
# mode.chained_assignment : string
#     Raise an exception, warn, or no action if trying to use chained assignment,
#     The default is warn
#     [default: warn] [currently: warn]
# mode.sim_interactive : boolean
#     Whether to simulate interactive mode for purposes of testing
#     [default: False] [currently: False]
# mode.use_inf_as_na : boolean
#     True means treat None, NaN, INF, -INF as NA (old way),
#     False means None and NaN are null, but INF, -INF are not NA
#     (new way).
#     [default: False] [currently: False]
# mode.use_inf_as_null : boolean
#     use_inf_as_null had been deprecated and will be removed in a future
#     version. Use `use_inf_as_na` instead.
#     [default: False] [currently: False]
#     (Deprecated, use `mode.use_inf_as_na` instead.)
# plotting.matplotlib.register_converters : bool
#     Whether to register converters with matplotlib's units registry for
#     dates, times, datetimes, and Periods. Toggling to False will remove
#     the converters, restoring any converters that pandas overwrote.
#     [default: True] [currently: True]

pd.describe_option('compute')
# compute.use_bottleneck : bool
#     Use the bottleneck library to accelerate if it is installed,
#     the default is True
#     Valid values: False,True
#     [default: True] [currently: True]
# compute.use_numexpr : bool
#     Use the numexpr library to accelerate computation if it is installed,
#     the default is True
#     Valid values: False,True
#     [default: True] [currently: True]

pd.describe_option('max_col')
# display.max_columns : int
#     If max_cols is exceeded, switch to truncate view. Depending on
#     `large_repr`, objects are either centrally truncated or printed as
#     a summary view. 'None' value means unlimited.
#     In case python/IPython is running in a terminal and `large_repr`
#     equals 'truncate' this can be set to 0 and pandas will auto-detect
#     the width of the terminal and print a truncated object which fits
#     the screen width. The IPython notebook, IPython qtconsole, or IDLE
#     do not run in a terminal and hence it is not possible to do
#     correct auto-detection.
#     [default: 20] [currently: 20]
# display.max_colwidth : int
#     The maximum width in characters of a column in the repr of
#     a pandas data structure. When the column overflows, a "..."
#     placeholder is embedded in the output.
#     [default: 50] [currently: 50]

pd.describe_option('max.*col')
# display.max_columns : int
#     If max_cols is exceeded, switch to truncate view. Depending on
#     `large_repr`, objects are either centrally truncated or printed as
#     a summary view. 'None' value means unlimited.
#     In case python/IPython is running in a terminal and `large_repr`
#     equals 'truncate' this can be set to 0 and pandas will auto-detect
#     the width of the terminal and print a truncated object which fits
#     the screen width. The IPython notebook, IPython qtconsole, or IDLE
#     do not run in a terminal and hence it is not possible to do
#     correct auto-detection.
#     [default: 20] [currently: 20]
# display.max_colwidth : int
#     The maximum width in characters of a column in the repr of
#     a pandas data structure. When the column overflows, a "..."
#     placeholder is embedded in the output.
#     [default: 50] [currently: 50]
# display.max_info_columns : int
#     max_info_columns is used in DataFrame.info method to decide if
#     per column information will be printed.
#     [default: 100] [currently: 100]

print(pd.get_option('display.max_rows'))
# 100

pd.set_option('display.max_rows', 60)

print(pd.get_option('max_r'))
# 60

pd.set_option('max_r', 100)

# pd.get_option('max')
# OptionError: 'Pattern matched multiple keys'

# pd.set_option('max', 60)
# OptionError: 'Pattern matched multiple keys'

l = ['display.max_rows', 'display.max_columns', 'display.max_colwidth']

print([pd.get_option(i) for i in l])
# [100, 20, 50]

print({i: pd.get_option(i) for i in l})
# {'display.max_rows': 100, 'display.max_columns': 20, 'display.max_colwidth': 50}

d = {'display.max_rows': 80,
     'display.max_columns': 80,
     'display.max_colwidth': 80}

[pd.set_option(k, v) for k, v in d.items()]

print({i: pd.get_option(i) for i in d.keys()})
# {'display.max_rows': 80, 'display.max_columns': 80, 'display.max_colwidth': 80}

print(pd.options.display.max_rows)
# 80

pd.reset_option('display.max_rows')

print(pd.options.display.max_rows)
# 60

print(pd.options.display.max_columns)
print(pd.options.display.max_colwidth)
# 80
# 80

pd.reset_option('max_col')

print(pd.options.display.max_columns)
print(pd.options.display.max_colwidth)
# 20
# 50

pd.options.display.max_rows = 100
pd.options.display.max_columns = 100
pd.options.display.max_colwidth = 100

pd.reset_option('^display', silent=True)

print(pd.options.display.max_rows)
print(pd.options.display.max_columns)
print(pd.options.display.max_colwidth)
# 60
# 20
# 50

pd.reset_option('all')
# html.border has been deprecated, use display.html.border instead
# (currently both are identical)
# : boolean
#     use_inf_as_null had been deprecated and will be removed in a future
#     version. Use `use_inf_as_na` instead.
# /usr/local/lib/python3.6/site-packages/pandas/core/config.py:619: FutureWarning: html.border has been deprecated, use display.html.border instead
# (currently both are identical)
#   warnings.warn(d.msg, FutureWarning)
# /usr/local/lib/python3.6/site-packages/pandas/core/config.py:619: FutureWarning: 
# : boolean
#     use_inf_as_null had been deprecated and will be removed in a future
#     version. Use `use_inf_as_na` instead.
#   warnings.warn(d.msg, FutureWarning)

pd.reset_option('all', silent=True)

with pd.option_context('display.max_rows', 100):
    print(pd.options.display.max_rows)
# 100

print(pd.options.display.max_rows)
# 60

pd.options.display.max_rows = 80

with pd.option_context('display.max_rows', 100):
    print(pd.options.display.max_rows)
# 100

print(pd.options.display.max_rows)
# 80

with pd.option_context('display.max_rows', 100, 'display.max_columns', 100):
    print(pd.options.display.max_rows)
    print(pd.options.display.max_columns)
# 100
# 100

print(pd.options.display.max_rows)
print(pd.options.display.max_columns)
# 80
# 20

pd.option_context('display.max_rows', 100)

print(pd.options.display.max_rows)
# 80
