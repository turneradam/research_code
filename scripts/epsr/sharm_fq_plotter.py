import pandas as pd
import numpy as np
import glob
import matplotlib.pyplot as plt

# experimental f(q)
files = glob.glob('*.x01') # file pattern something like '*.csv'
# EPSR simulated f(q) 
sdata = glob.glob('*.w01')

xfile = np.loadtxt(files[0].strip(), unpack=True)
xvals = pd.DataFrame(data=xfile[0:1,:])
xvals = xvals.T

rdfs = pd.DataFrame()

i = 1
for file in files:
    df1 = np.loadtxt(file.strip(), unpack=True)
    rdf = pd.DataFrame(data=df1[1:,:])
    rdf += i
    rdfs = rdfs.append(rdf)
    i += 1

rdfs = rdfs.T
#rdfs += 1

xvals.columns = [0]
rdfs.columns = files

sharms = pd.concat([xvals, rdfs], axis=1)
sharms.plot.line(x=0)

# plot related labels
plt.xlabel('$\mathrm{\it{r\,/\,\AA}}$')
plt.ylabel('$\it{g(r)}$')

#plt.legend(files, loc=0)
# show the plot for viewing
plt.show()
