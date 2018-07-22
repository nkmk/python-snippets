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
# target_path_1:  data/src/test.txt
# read target file:
# line 1
# line 2
# line 3
# 
# [set target path 2]
# target_path_2:  data/src/../dst/test_new.json
# read target file:
# {
#   "A": 100,
#   "B": "abc",
#   "C": "あいうえお"
# }
# 
# [change directory]
# getcwd:       /Users/mbp/Documents/my-project/python-snippets/notebook/data/src
# 
# [set target path 1 (after chdir)]
# target_path_1:  test.txt
# read target file:
# line 1
# line 2
# line 3
# 
# [set target path 2 (after chdir)]
# target_path_2:  ../dst/test_new.json
# read target file:
# {
#   "A": 100,
#   "B": "abc",
#   "C": "あいうえお"
# }

cd data/src

python3 file_path.py
# getcwd:       /Users/mbp/Documents/my-project/python-snippets/notebook/data/src
# __file__:     file_path.py
# basename:     file_path.py
# dirname:      
# abspath:      /Users/mbp/Documents/my-project/python-snippets/notebook/data/src/file_path.py
# abs dirname:  /Users/mbp/Documents/my-project/python-snippets/notebook/data/src
# 
# [set target path 1]
# target_path_1:  test.txt
# read target file:
# line 1
# line 2
# line 3
# 
# [set target path 2]
# target_path_2:  ../dst/test_new.json
# read target file:
# {
#   "A": 100,
#   "B": "abc",
#   "C": "あいうえお"
# }
# 
# [change directory]
# getcwd:       /Users/mbp/Documents/my-project/python-snippets/notebook/data/src
# 
# [set target path 1 (after chdir)]
# target_path_1:  test.txt
# read target file:
# line 1
# line 2
# line 3
# 
# [set target path 2 (after chdir)]
# target_path_2:  ../dst/test_new.json
# read target file:
# {
#   "A": 100,
#   "B": "abc",
#   "C": "あいうえお"
# }
