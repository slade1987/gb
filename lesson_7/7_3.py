import os
import shutil

os_path = os.getcwd()
directory = os.path.join(os_path,'my_project')
directory = os.path.join(directory,'templates\\')
print(directory)

dic_path = {}

k = os.walk('my_project')
for i in k:
    if i[0].endswith('templates'):
        for j in os.walk(i[0]):
            if not j[0].endswith('templates'):
                str_res = j[0].split('\\')
                str_res = str_res[-1]
                directory1 = os.path.join(directory,str_res)
                dic_path[j[0]] = directory1

os.makedirs(directory)
print(dic_path)
for key, val in dic_path.items():
    shutil.copytree(key, val)

