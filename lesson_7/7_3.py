import os
import shutil


os_path = os.getcwd()
directory = os.path.join(os_path,'my_project')
directory = os.path.join(directory,'templates\\')
print(directory)
'''
s.makedirs(directory)

'''

k = os.walk('my_project')
for i in k:
    if i[0].endswith('templates'):
        for j in os.walk(i[0]):
            print(j)
            #shutil.copytree(j,directory)
#'''