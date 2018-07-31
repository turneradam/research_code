import pandas as pd
import numpy as np
from sys import argv
from matplotlib import pyplot as mp
import os

clean_data = pd.read_csv("data_noisifier.csv")
print(clean_data.head())

mu, sigma = 0,0.1
noise = np.random.normal(mu, sigma, clean_data.shape)
random_noise = pd.DataFrame(data=noise)
print(random_noise.head())

noisy_data = clean_data.add(random_noise, fill_value=0)
print(noisy_data.head())

noisy_data.to_csv()

# Write the output of the normalisation to a new CSV file with name
# $file_area_norm.csv
# Create the output file name for the CSV
out_filename = 'out_' + str(argv[1])
# Write the normalised data to a file with name out_filename.csv
noisy_data.to_csv(out_filename,header=False,index=False)
