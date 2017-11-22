import os

for filename in os.listdir("."):
    if filename.endswith("(FDS).TXT"):
        os.rename(filename, filename[:-9] + ".txt")
