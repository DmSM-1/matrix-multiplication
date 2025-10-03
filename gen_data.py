import numpy as np
import os
import shutil

sizes = [32, 64, 128, 256, 512, 1024, 2048]
n = 1

if os.path.exists("DATA"):
    shutil.rmtree("DATA")

os.makedirs("DATA")

for i in sizes:
    for j in range(n):
        os.system(f"py gen.py {i} DATA/A{i}_{j} DATA/B{i}_{j} DATA/C{i}_{j}")
        print(f"py gen.py {i} DATA/A{i}_{j} DATA/B{i}_{j} DATA/C{i}_{j}")
