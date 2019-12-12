from pathlib import Path
from time import ctime

#  generic useful methods for dealing with files
path = Path(r'..\ecommerce_modules\__init__.py')
#  the path.stat() method returns a lot of useful stats about the file
print(f'Creation Time: {ctime(path.stat().st_ctime)}')
path.read_bytes()
print('File contents:', path.read_text())
