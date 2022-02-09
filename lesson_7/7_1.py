import os


def ensure_dir(file_path, new_dir):
    directory = os.path.join(file_path, new_dir)
    if not os.path.exists(directory):
        os.makedirs(directory)


project = {'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}
os_path = os.getcwd()

for key, val in project.items():
    ensure_dir(os_path, key)
    for item in range(len(val)):
        ensure_dir(os.path.join(os_path, key), val[item])
