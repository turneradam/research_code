import os
import sys
import pandas as pd

# First line if header, second if none
#csvfile = pd.read_csv(sys.argv[1], header=None)
csvfile = pd.read_csv(sys.argv[1])

x = csvfile.iloc[:,0]
xfile = pd.DataFrame([x]).T

set_file = []

i = 1
frange = csvfile.shape[1] - 1
for i in range(frange):
    for column in csvfile:
        y = csvfile.iloc[:,i]
        yfile = pd.DataFrame([y]).T
        ofile = pd.concat([xfile,yfile], join="inner", axis=1)
        ofile_name = str(i) + '_' + str(sys.argv[1])
        print(ofile_name)
        ofile.to_csv(ofile_name, header=False, index=False)
        set_file.append(ofile_name)
        i += 1
    set = pd.DataFrame(set_file)
    set.to_csv('setfile.set', header=False, index=False)
