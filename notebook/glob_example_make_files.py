import os

os.makedirs('temp/dir', exist_ok=True)

with open('temp/012.txt', 'w') as f:
    pass

with open('temp/abc.txt', 'w') as f:
    pass

with open('temp/file.text', 'w') as f:
    pass

with open('temp/dir/789.txt', 'w') as f:
    pass

with open('temp/dir/xyz.text', 'w') as f:
    pass
