import pandas as pd
import numpy as np
import glob
import matplotlib.pyplot as plt
from sys import argv

files = glob.glob('*.h01')# file pattern something like '*.csv'

xfile = np.loadtxt(files[0].strip(), unpack=True)
xvals = pd.DataFrame(data=xfile[0:1,:])
xvals = xvals.T

rdfs = pd.DataFrame()

for file in files:
    df1 = np.loadtxt(file.strip(), unpack=True)
    rdf = pd.DataFrame(data=df1[1:2,:])
    rdfs = rdfs.append(rdf)

rdfs = rdfs.T
rdfs += 1

xvals.columns = [0]
rdfs.columns = files

sharms = pd.concat([xvals, rdfs], axis=1)
sharms.plot.line(x=0)

# plot related labels
plt.xlabel('$\mathrm{\it{r\,/\,\AA}}$')
plt.ylabel('$\it{g(r)}$')
plt.axis([0, 18, 0, 4]) # axis as a list [x1, x2, y1, y2]

# extra data labels
label_file = open(argv[2])
labels = []
for line in label_file:
    line = line[:-1] # remove the \n character
    labels.append(line)

#plt.legend(files, loc=0)
plt.legend(labels)
# save the figure as a png
plt.savefig(argv[1], dpi=600)
# show the plot for viewing
plt.show()
