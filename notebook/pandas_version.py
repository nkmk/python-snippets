import pandas as pd

print(pd.__version__)
# 2.0.1

pd.show_versions()
# 
# INSTALLED VERSIONS
# ------------------
# commit           : 37ea63d540fd27274cad6585082c91b1283f963d
# python           : 3.11.3.final.0
# python-bits      : 64
# OS               : Darwin
# OS-release       : 22.4.0
# Version          : Darwin Kernel Version 22.4.0: Mon Mar  6 21:01:02 PST 2023; root:xnu-8796.101.5~3/RELEASE_ARM64_T8112
# machine          : arm64
# processor        : arm
# byteorder        : little
# LC_ALL           : None
# LANG             : ja_JP.UTF-8
# LOCALE           : ja_JP.UTF-8
# 
# pandas           : 2.0.1
# numpy            : 1.24.3
# pytz             : 2022.7.1
# dateutil         : 2.8.2
# setuptools       : 67.6.1
# pip              : 23.1.2
# Cython           : None
# pytest           : None
# hypothesis       : None
# sphinx           : None
# blosc            : None
# feather          : None
# xlsxwriter       : None
# lxml.etree       : 4.9.2
# html5lib         : None
# pymysql          : None
# psycopg2         : None
# jinja2           : 3.1.2
# IPython          : 8.13.1
# pandas_datareader: None
# bs4              : 4.11.2
# bottleneck       : None
# brotli           : None
# fastparquet      : None
# fsspec           : None
# gcsfs            : None
# matplotlib       : None
# numba            : None
# numexpr          : None
# odfpy            : None
# openpyxl         : None
# pandas_gbq       : None
# pyarrow          : None
# pyreadstat       : None
# pyxlsb           : None
# s3fs             : None
# scipy            : None
# snappy           : None
# sqlalchemy       : None
# tables           : None
# tabulate         : None
# xarray           : None
# xlrd             : None
# zstandard        : None
# tzdata           : 2023.3
# qtpy             : None
# pyqt5            : None
# 
# /opt/homebrew/Cellar/python@3.11/3.11.3/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/_distutils_hack/__init__.py:33: UserWarning: Setuptools is replacing distutils.
#   warnings.warn("Setuptools is replacing distutils.")

pd.show_versions(True)
# {
#   "system": {
#     "commit": "37ea63d540fd27274cad6585082c91b1283f963d",
#     "python": "3.11.3.final.0",
#     "python-bits": 64,
#     "OS": "Darwin",
#     "OS-release": "22.4.0",
#     "Version": "Darwin Kernel Version 22.4.0: Mon Mar  6 21:01:02 PST 2023; root:xnu-8796.101.5~3/RELEASE_ARM64_T8112",
#     "machine": "arm64",
#     "processor": "arm",
#     "byteorder": "little",
#     "LC_ALL": null,
#     "LANG": "ja_JP.UTF-8",
#     "LOCALE": {
#       "language-code": "ja_JP",
#       "encoding": "UTF-8"
#     }
#   },
#   "dependencies": {
#     "pandas": "2.0.1",
#     "numpy": "1.24.3",
#     "pytz": "2022.7.1",
#     "dateutil": "2.8.2",
#     "setuptools": "67.6.1",
#     "pip": "23.1.2",
#     "Cython": null,
#     "pytest": null,
#     "hypothesis": null,
#     "sphinx": null,
#     "blosc": null,
#     "feather": null,
#     "xlsxwriter": null,
#     "lxml.etree": "4.9.2",
#     "html5lib": null,
#     "pymysql": null,
#     "psycopg2": null,
#     "jinja2": "3.1.2",
#     "IPython": "8.13.1",
#     "pandas_datareader": null,
#     "bs4": "4.11.2",
#     "bottleneck": null,
#     "brotli": null,
#     "fastparquet": null,
#     "fsspec": null,
#     "gcsfs": null,
#     "matplotlib": null,
#     "numba": null,
#     "numexpr": null,
#     "odfpy": null,
#     "openpyxl": null,
#     "pandas_gbq": null,
#     "pyarrow": null,
#     "pyreadstat": null,
#     "pyxlsb": null,
#     "s3fs": null,
#     "scipy": null,
#     "snappy": null,
#     "sqlalchemy": null,
#     "tables": null,
#     "tabulate": null,
#     "xarray": null,
#     "xlrd": null,
#     "zstandard": null,
#     "tzdata": "2023.3",
#     "qtpy": null,
#     "pyqt5": null
#   }
# }

pd.show_versions('data/temp/pandas_versions.txt')
