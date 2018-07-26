# TODO:
# 1) Comment code
# 2) Write normalised data to CSV
# 3) Determine if trapz or simps is more accurate
# 4) Loop over all columns in spectra CSV

from sys import argv
from matplotlib import pyplot as mp
import pandas as pd
import numpy as np
from scipy import integrate as sp

# Read the csv file, then assign no header so reads first row as data
spectra = pd.read_csv(argv[1], header=None)
print(spectra)

# Assign the first column to X axis values
x = spectra.iloc[:,0]

# Assign the second colum as y values
y = spectra.iloc[:,1]
print("This is column")
print(y)

# Integrate over all the y values using the trapezoidal rule and then normalise
# by area
areaT = np.trapz(y)
y_normT = y / areaT

# Integrate over all y values using Simpson integration and then normalise by
# area
areaS = sp.simps(y)
y_normS = y / areaS

print(areaT)
print(areaS)

# Plot the output of normalisation using both the trapezoidal rule and the
# Simpson rule
mp.plot(x,y_normT,x,y_normS,linewidth=2.0)
mp.show()
