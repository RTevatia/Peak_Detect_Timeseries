import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def peak_find(data, window_size):
    """
    find values and positions of peaks in a given time series data. 
    return a list of tuples [(x1, max1), (x2, max2),..,(xn, maxn)]
    
    data: a given time series data
    window_size: look for peaks in a box of "window_size" size

    """
    data_extended = np.concatenate([np.zeros(window_size), data, np.zeros(window_size)])
    max_list = []

    for i, _ in enumerate(data_extended):
        if (i >= window_size) and (i < len(data_extended) - window_size):
            try:
                max_left = data_extended[(i - window_size) : i + 1].max()
                max_right = data_extended[i : (i + window_size) + 1].max()
                check_value = data_extended[i] - ((max_left + max_right) / 2)
            except ValueError:
                pass

            if check_value >= 0:
                max_list.append((i - window_size, data[(i - window_size)]))
    return max_list


def calculate_peak_timestamps(timestamps, peaks_list):
    """
    Calculate the timestamps for each peak.

    Parameters:
    - timestamps: The timestamps corresponding to each data point in the series
    - peaks: The list of peak positions from peak_finding
    
    Returns:
    - List of timestamps corresponding to each peak
    """
    return [timestamps[pos] for pos, _ in peaks_list]


def convert_to_df(peaks, timestamps):
    """
    Store the peaks information to Panda's dataframe.

    Parameters:
    - peaks: The list of peaks (position and value)
    - timestamps: The timestamps corresponding to each peak
    """
    df = pd.DataFrame(peaks, columns=["Position", "Value"])
    df["Timestamp"] = timestamps
    return df


def save_peaks_to_csv(df, filename="peaks.csv"):
    """
    Save the peaks information to a CSV file.

    Parameters:
    - peaks: The list of peaks (position and value)
    - timestamps: The timestamps corresponding to each peak
    - filename: The name of the file to save the peaks information
    """
    df.to_csv(filename, index=False)


def plot_peaks(data_time, data_value, peaks_time, peaks_value, xlabel, ylabel, title):
    """
    Plot the peaks on time series data
    """
    _ , ax = plt.subplots()
    ax.set_ylabel(ylabel)
    ax.set_xlabel(xlabel)
    ax.set_title(title)
    ax.plot(data_time, data_value, color="red")
    ax.scatter(peaks_time, peaks_value, color="green")
    plt.show()
    