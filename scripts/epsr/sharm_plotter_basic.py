import pandas as pd
import numpy as np
import glob
import matplotlib.pyplot as plt

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

plt.legend(files, loc=0)
# show the plot for viewing
plt.show()
