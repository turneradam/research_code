# TODO:
# 1) Comment code - DONE
# 2) Write normalised data to CSV - DONE
# 3) Determine if trapz or simps is more accurate - So long as we remain
# consistent, ie. trapz of trapz data or simps of simps data then the area will
# be equal to 1. Otherwise we will introduce error.
# 4) Loop over all columns in spectra CSV - DONE
# 5) Split out into decorators
# 6) Modularise the program
# 7) Spin this out into separate programs
# 8) First value after x column in output is normalised x axis fix this

import sys
import pandas as pd
import numpy as np
from scipy import integrate as sp

def input_validator(func):
    # TODO: Spin this out into a decorator
    print("checking inputs\n")
    if len(sys.argv) < 2:
        print("Error::: Parse File not defined")
        sys.exit(1)

    if OUTPUT_FILE not in os.listdir():
        print("ERROR::: File does not exist")
        sys.exit(1)
    
    def wrapped():
        func()

    return wrapped
# Read the csv file, then assign no header so reads first row as data
spectra = pd.read_csv(sys.argv[1], header=None)

print(spectra)
# Assign the first column to X axis values
x = spectra.iloc[:,0]

# Integrate over all the y values using the trapezoidal rule and then normalise
# by area
def normaliser(y_values):
    areaS = sp.simps(y_values)
    y_normS = y_values / areaS
    return y_normS

iter_spectra = spectra.to_records()

normalised_spectra = pd.DataFrame([x]).T

# Do normalisation of the data and then append it to the data frame for all the
# normalised data. First it sets the index to 1 so as not to normalise the x
# axis and then iterates over all the columns in the csv appending the relevant
# value from each row list. Finally the normalised data is appended to the
# dataframe and the column incrementer is increased.
# By setting col=2 then we avoid normalising the x-axis but this seems like a
# fudge
col = 2
while col < len(iter_spectra[0]):
    spec_data = []
    for row in iter_spectra:
        spec_data.append(row[col])
    spec_data = normaliser(spec_data)
    spec_data = pd.DataFrame(data=spec_data)
    normalised_spectra = pd.concat([normalised_spectra,spec_data], join="inner", axis=1)
    col += 1    

print(normalised_spectra)
# Write the output of the normalisation to a new CSV file with name
# $file_area_norm.csv
# Create the output file name for the CSV
out_filename = 'out_' + str(sys.argv[1])
# Write the normalised data to a file with name out_filename.csv
normalised_spectra.to_csv(out_filename,header=False,index=False)

# Plot the output of normalisation using both the trapezoidal rule and the
# Simpson rule
#mp.plot(x,y_normT,x,y_normS,linewidth=2.0)
#mp.show()
