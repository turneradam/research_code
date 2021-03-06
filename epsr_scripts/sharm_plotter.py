import pandas as pd
import numpy as np
import glob
import matplotlib.pyplot as plt

files = glob.glob('*.h01')# file pattern something like '*.csv'

rdfs = pd.DataFrame(columns = files)
print(files)

for file in files:
    df1 = np.loadtxt(file.strip(), unpack=True)
    rdf = pd.DataFrame(data=df1[1:2,:])
    rdfs = rdfs.append(rdf)


rdfs = rdfs.T

#rdfs.plot.line(x=1, y=1)
rdfs.plot.line()

# plot related labels
plt.xlabel('$\mathrm{\it{r\,/\,\AA}}$')
plt.ylabel('$\it{g(r)}$')

plt.legend(files, loc=0)
# show the plot for viewing
plt.show()
