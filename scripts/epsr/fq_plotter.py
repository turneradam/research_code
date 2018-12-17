import pandas as pd
import numpy as np
import glob
import matplotlib.pyplot as plt

# experimental f(q)
xdata = glob.glob('*.x01') # file pattern something like '*.csv'
# EPSR simulated f(q) 
wdata = glob.glob('*.w01')

xfile = np.loadtxt(xdata[0].strip(), unpack=True)
xvals = pd.DataFrame(data=xfile[0:1,:])
xvals = xvals.T


def slicer(files):
    """
    xfile = np.loadtxt(files[0].strip(), unpack=True)
    xvals = pd.DataFrame(data=xfile[0:1,:])
    xvals = xvals.T
    """

    rdfs = pd.DataFrame()
    for file in files:
        df1 = np.loadtxt(file.strip(), unpack=True)
        # read the data minus the first column
        rdf = pd.DataFrame(data=df1[1:,:])
        rdfs = rdfs.append(rdf)

    # slice out the error columns
    rdfs = rdfs[::2]
    rdfs = rdfs.T
    return rdfs
    """
    plot_data = pd.concat([xvals, slicer(rdfs)], axis=1)
    return plot_data
    """

plot_xdata = pd.concat([xvals, slicer(xdata)], axis=1)
plot_xdata.columns = list(range(0,len(plot_xdata.T)))

plot_wdata = pd.concat([xvals, slicer(wdata)], axis=1)
plot_wdata.columns = list(range(0,len(plot_wdata.T)))

#xvals.columns = [0]
#plot_xdata.columns = xdata
"""
xdata_plot = slicer(xdata)
print(xdata_plot)
"""

ax = plot_xdata.plot(x=0)
plot_wdata.plot(ax=ax, x=0)
plt.axis([0, 18, 0, 4]) # axis as a list [x1, x2, y1, y2]

#sharms = pd.concat([xvals, rdfs], axis=1)
#plot_xdata.plot.line(x=0)
#plot_wdata.plot.line(x=0)
#slicer(xdata).plot.line()

# plot related labels
plt.xlabel('$\mathrm{\it{r\,/\,\AA}}$')
plt.ylabel('$\it{g(r)}$')

#plt.legend(files, loc=0)
# show the plot for viewing
plt.show()
