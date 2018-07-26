# TODO:
# 1) Comment code - DONE
# 2) Write normalised data to CSV
# 3) Determine if trapz or simps is more accurate - So long as we remain
# consistent, ie. trapz of trapz data or simps of simps data then the area will
# be equal to 1. Otherwise we will introduce error.
# 4) Loop over all columns in spectra CSV

from sys import argv
from matplotlib import pyplot as mp
import pandas as pd
import numpy as np
from scipy import integrate as sp

# Read the csv file, then assign no header so reads first row as data
spectra = pd.read_csv(argv[1], header=None)
#print(spectra)

# Assign the first column to X axis values
x = spectra.iloc[:,0]

# Assign the second colum as y values
y = spectra.iloc[:,1]

# Integrate over all the y values using the trapezoidal rule and then normalise
# by area
areaT = np.trapz(y)
y_normT = y / areaT

# Integrate over all y values using Simpson integration and then normalise by
# area
areaS = sp.simps(y)
y_normS = y / areaS

# Append X and Y normalised values to a new dataframe
# Create a list of the values to be in the CSV
frames = [x,y_normS]
# Concatenate the datasets with the x-axis
results = pd.concat(frames, axis=1, join='outer')

# Write the output of the normalisation to a new CSV file with name
# $file_area_norm.csv
# Create the output file name for the CSV
out_filename = 'out_' + str(argv[1])
# Write the normalised data to a file with name out_filename.csv
results.to_csv(out_filename,header=False,index=False)

# Plot the output of normalisation using both the trapezoidal rule and the
# Simpson rule
#mp.plot(x,y_normT,x,y_normS,linewidth=2.0)
#mp.show()
