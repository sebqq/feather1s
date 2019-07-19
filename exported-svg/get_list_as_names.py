import os

names = []
for dirpath, dnames, fnames in os.walk("./"):
    for f in fnames:
        if f.endswith(".svg"):
          new_name = f.replace(".svg", "")
          names.append(new_name)

from pprint import pprint
pprint(names)
print()
print(len(names))