import os
import sys
import pandas as pd

if len(sys.argv) != 3:
    sys.exit(-1)

csv = sys.argv[1]
location = sys.argv[2]

df = pd.read_csv(csv)

old_names = df["old_name"]
new_names = df["new_name"]

for i, val in enumerate(old_names, start=1):
    os.rename(f"{location}/{val}.txt", f"{location}/temp{i}.txt")
    if i == len(old_names):
        for j, dist in enumerate(new_names, start=1):
            os.rename(f"{location}/temp{j}.txt", f"{location}/{dist}.txt")

