import os
from collections import defaultdict
import shutil

import django

'''
os_path = os.getcwd()
print(os_path)
print(os.path.getsize(os.path.join(os_path,'7_1.py')))





'''
root_dir = django.__path__[0]
django_files = defaultdict(list)
for root, dirs, files in os.walk(root_dir):
    for end_dirs in dirs:
        for end_file in files:
            os_path = os.path.join(str(root),str(end_dirs))
            os_path = os.path.join(os_path,str(end_file))
            print(os_path)



#   for file in files:
#        os.sta

