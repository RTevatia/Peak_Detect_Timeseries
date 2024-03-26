import matplotlib.pyplot as plt
import pandas as pd
import peak_func as pf

# Load data
milk_data = pd.read_csv("milk_production.csv")
milk_data.head()

# Get the time series from the data
time_series = milk_data["Monthly milk production (pounds per cow)"]

# Find peaks with a windows size of 4
peaks_list_4 = pf.peak_finding(time_series, 4)
x_peaks_4 = [x for x, y in peaks_list_4]
y_peaks_4 = [y for x, y in peaks_list_4]

# Plotting
pf.plot_peaks(time_series, 4, "blue", "Monthly milk production\nPeaks with window size of 4")
pf.plot_peaks(time_series, 1, "green", "Monthly milk production\nPeaks with window size of 1")
