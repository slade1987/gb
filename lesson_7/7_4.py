import os
import django

diction = {}

root_dir = django.__path__[0]
print(root_dir)
for root, dirs, files in os.walk(root_dir):
    for file in files:
        real_path = os.path.join(root,file)
        size =10 ** len(str(os.stat(real_path).st_size))
        if  size in diction.keys():
            diction[size] += 1
        else:
            diction[size] = 1

for size, nums in sorted(diction.items()):
    print(size, '   ', nums)
