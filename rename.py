import os

path = "F:/traindata/pabonsir/450rpm/Keppler"

folder = os.listdir(path)
# print(folder)

for folders in folder:
    os.rename(os.path.join(path, folders), os.path.join(path, folders.replace("antares", "keppler")))
