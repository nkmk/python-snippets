import zipfile

with zipfile.ZipFile('data/temp/new_comp.zip', 'w', compression=zipfile.ZIP_DEFLATED) as new_zip:
    new_zip.write('data/temp/test1.txt', arcname='test1.txt')
    new_zip.write('data/temp/test2.txt', arcname='zipdir/test2.txt')
    new_zip.write('data/temp/test3.txt', arcname='zipdir/sub_dir/test3.txt')

with zipfile.ZipFile('data/temp/new_comp_single.zip', 'w') as new_zip:
    new_zip.write('data/temp/test1.txt', arcname='test1.txt', compress_type=zipfile.ZIP_DEFLATED)
    new_zip.write('data/temp/test2.txt', arcname='zipdir/test2.txt')
    new_zip.write('data/temp/test3.txt', arcname='zipdir/sub_dir/test3.txt')

with zipfile.ZipFile('data/temp/new_comp.zip', 'a') as existing_zip:
    existing_zip.write('data/temp/test4.txt', arcname='test4.txt')

with zipfile.ZipFile('data/temp/new_comp.zip') as existing_zip:
    print(existing_zip.namelist())
# ['test1.txt', 'zipdir/test2.txt', 'zipdir/sub_dir/test3.txt', 'test4.txt']

with zipfile.ZipFile('data/temp/new_comp.zip') as existing_zip:
    existing_zip.extractall('data/temp/ext')

with zipfile.ZipFile('data/temp/new_comp_with_pass.zip') as pass_zip:
    pass_zip.extractall('data/temp/ext_pass', pwd='password')

with zipfile.ZipFile('data/temp/new_comp.zip') as existing_zip:
    existing_zip.extract('test1.txt', 'data/temp/ext2')

with zipfile.ZipFile('data/temp/new_comp_with_pass.zip') as pass_zip:
    pass_zip.extract('test1.txt', 'data/temp/ext_pass2', pwd='password')
