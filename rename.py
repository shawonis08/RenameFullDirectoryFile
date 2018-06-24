import os

path = ""

folder = os.listdir(path)

for folders in folder:
    os.rename(os.path.join(path,folder), os.path.join(path,folder.replace('orginalName', 'changename')))
