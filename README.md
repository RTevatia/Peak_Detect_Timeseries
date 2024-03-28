# Peak Detection using Python

## Description
 A simple python program to find values and positions of peaks in a given time series.
 Further, this program helps to plot peaks over the timeseries data.

### peak_func.py module
 This module contains several function that help to detect, plot and save peak values and positions.
#### a. peak_find:
"peak_finding" function can be used to find the values and positions of peaks in a timeseries data.
#### b. calculate_peak_timestamps
"calculate_peak_timestamps" function detects the position i.e. timestamps for each peak.
#### c. convert_to_df
"covert_to_df" function add the values of peak_find and their respective positions in a dataframe.
#### d. save_peaks_to_csv
"save_peaks_to_csv" function store above created df into a csv file.
### plot_peaks
"plot_peaks" function plots the peaks over the data

### peaks_detect.py
This is the main python file that is used to identify peaks for the data "milk_production.csv".

## Installation
1. Clone the repository: git clone 
2. Navigate to the repository: cd your_repository
3. Install dependencies: npm install

## Usage
Step 1. Data - The data csv file 'milk_production.csv' is included (reference given below). To use the script, include your data and change filename in 'peak_detect.py' for Load data. Your data must be formatted in - Data#, timestamp, data_value. The formatted csv file can be used as is or if data is in excel sheet, please change "pd.read_csv" to "pd.read_excel" and include your excel filename.
Step 2. Run 'peaks_detect.py' - Running the script will provide peaks locations. A graph will appear for visual inspection if peaks have been detected correctly or not. Change the window size. Smaller window size will detect more peaks, and may include residual peaks. Thus, the window size threshold shall be decided carefully.
These two graphs were prepared by the script for the included data and window size 
![Figure_1](https://github.com/RTevatia/Peakdetect/assets/11818993/5d6acbc8-4a46-4336-982a-aeb55271bf36)
![Figure_1](https://github.com/RTevatia/Peakdetect/assets/11818993/b9daec47-850d-4b16-84e1-9690412ab43e)


## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!
    
 ## Reference
 https://www.researchgate.net/profile/Girish_Palshikar/publication/228853276_Simple_Algorithms_for_Peak_Detection_in_Time-Series/links/53fd70ca0cf2364ccc08c4d8.pdf

