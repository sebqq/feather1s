import os

PATH_TO_SVG_FOLDER = "./exported-svg"

names = []
for dirpath, dnames, fnames in os.walk(PATH_TO_SVG_FOLDER):
    for f in fnames:
        if f.endswith(".svg"):
          new_name = f.replace(".svg", "")
          names.append(new_name)

from pprint import pprint
pprint(names)
print()
print(len(names))