pwd
# /Users/mbp/Documents/my-project/python-snippets/notebook

python3 data/src/file_path.py
# getcwd:       /Users/mbp/Documents/my-project/python-snippets/notebook
# __file__:     data/src/file_path.py
# basename:     file_path.py
# dirname:      data/src
# abspath:      /Users/mbp/Documents/my-project/python-snippets/notebook/data/src/file_path.py
# abs dirname:  /Users/mbp/Documents/my-project/python-snippets/notebook/data/src
# 
# [set target path 1]
# target_path_1:  data/src/target_1.txt
# read target file:
# !! This is "target_1.txt" !!
# 
# [set target path 2]
# target_path_2:  data/src/../dst/target_2.txt
# normalize    :  data/dst/target_2.txt
# read target file:
# !! This is "target_2.txt" !!
# 
# [change directory]
# getcwd:       /Users/mbp/Documents/my-project/python-snippets/notebook/data/src
# 
# [set target path 1 (after chdir)]
# target_path_1:  target_1.txt
# read target file:
# !! This is "target_1.txt" !!
# 
# [set target path 2 (after chdir)]
# target_path_2:  ../dst/target_2.txt
# read target file:
# !! This is "target_2.txt" !!

pwd
# /Users/mbp/Documents/my-project/python-snippets/notebook

python3 /Users/mbp/Documents/my-project/python-snippets/notebook/data/src/file_path.py
# getcwd:       /Users/mbp/Documents/my-project/python-snippets/notebook
# __file__:     /Users/mbp/Documents/my-project/python-snippets/notebook/data/src/file_path.py
# basename:     file_path.py
# dirname:      /Users/mbp/Documents/my-project/python-snippets/notebook/data/src
# abspath:      /Users/mbp/Documents/my-project/python-snippets/notebook/data/src/file_path.py
# abs dirname:  /Users/mbp/Documents/my-project/python-snippets/notebook/data/src
# 
# [set target path 1]
# target_path_1:  /Users/mbp/Documents/my-project/python-snippets/notebook/data/src/target_1.txt
# read target file:
# !! This is "target_1.txt" !!
# 
# [set target path 2]
# target_path_2:  /Users/mbp/Documents/my-project/python-snippets/notebook/data/src/../dst/target_2.txt
# normalize    :  /Users/mbp/Documents/my-project/python-snippets/notebook/data/dst/target_2.txt
# read target file:
# !! This is "target_2.txt" !!
# 
# [change directory]
# getcwd:       /Users/mbp/Documents/my-project/python-snippets/notebook/data/src
# 
# [set target path 1 (after chdir)]
# target_path_1:  target_1.txt
# read target file:
# !! This is "target_1.txt" !!
# 
# [set target path 2 (after chdir)]
# target_path_2:  ../dst/target_2.txt
# read target file:
# !! This is "target_2.txt" !!

cd data/src

pwd
# /Users/mbp/Documents/my-project/python-snippets/notebook/data/src

python3 file_path.py
# getcwd:       /Users/mbp/Documents/my-project/python-snippets/notebook/data/src
# __file__:     file_path.py
# basename:     file_path.py
# dirname:      
# abspath:      /Users/mbp/Documents/my-project/python-snippets/notebook/data/src/file_path.py
# abs dirname:  /Users/mbp/Documents/my-project/python-snippets/notebook/data/src
# 
# [set target path 1]
# target_path_1:  target_1.txt
# read target file:
# !! This is "target_1.txt" !!
# 
# [set target path 2]
# target_path_2:  ../dst/target_2.txt
# normalize    :  ../dst/target_2.txt
# read target file:
# !! This is "target_2.txt" !!
# 
# [change directory]
# getcwd:       /Users/mbp/Documents/my-project/python-snippets/notebook/data/src
# 
# [set target path 1 (after chdir)]
# target_path_1:  target_1.txt
# read target file:
# !! This is "target_1.txt" !!
# 
# [set target path 2 (after chdir)]
# target_path_2:  ../dst/target_2.txt
# read target file:
# !! This is "target_2.txt" !!
