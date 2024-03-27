import matplotlib.pyplot as plt
import pandas as pd
import peak_func as pf

# Load data
milk_data = pd.read_csv("milk_production.csv")

# Get the time series from the data
data_series = milk_data["Monthly milk production (pounds per cow)"]
window_size = 4
timestamps = milk_data["Month"]

# Finding peaks
peaks_list = pf.peak_find(data_series, window_size)

# Calculating timestamps for peaks
peak_timestamps = pf.calculate_peak_timestamps(timestamps, peaks_list)

# store peak information with timestamps in a dataframe
df = pf.convert_to_df(peaks_list, peak_timestamps)
print(df)

# Saving peaks to CSV (uncomment next line to save peaks in a csv)
# pf.save_peaks_to_csv(df, filename=f"peaks_with_window_size_of_{window_size}.csv")

# Plotting for peaks calucalted for window size of 1
pf.plot_peaks(pd.to_datetime(timestamps),
 data_series, df["Timestamp"], df["Value"], 
 xlabel="Time", ylabel="Milk Production (pounds per cow)", 
 title=f"Monthly milk production\nPeaks with window size of {window_size}")

