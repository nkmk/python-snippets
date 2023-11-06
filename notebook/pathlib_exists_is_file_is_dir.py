from pathlib import Path

p_file = Path('data/temp/dir/file.txt')
p_dir = Path('data/temp/dir')
p_non_existent = Path('non_exist')

p_dir.mkdir(parents=True, exist_ok=True)
p_file.touch()

print(p_file.is_file())
# True

print(p_dir.is_file())
# False

print(p_non_existent.is_file())
# False

print(p_file.is_dir())
# False

print(p_dir.is_dir())
# True

print(p_non_existent.is_dir())
# False

print(p_file.exists())
# True

print(p_dir.exists())
# True

print(p_non_existent.exists())
# False

print(Path('data/temp/dir') == Path('data/temp/dir/'))
# True
