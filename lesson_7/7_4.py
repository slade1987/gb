import os
from collections import defaultdict

import django

root_dir = django.__path__[0]
print(root_dir)
django_files = defaultdict(list)
for root, dirs, files in os.walk(root_dir):
    for file in files:
        real_path = os.path.join(root,file)
        size = os.stat(real_path).st_size
        print(size)
