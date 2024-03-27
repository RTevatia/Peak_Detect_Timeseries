# Peak Detection / Peak Finding in Python

## Introduction
 A simple python program to find values and positions of peaks in a given time series.
 Further, this program helps to plot peaks over the timeseries data.

## peak_func.py module
 This module contains several function that help to detect, plot and save peak values and positions.
### a. peak_find:
"peak_finding" function can be used to find the values and positions of peaks in a timeseries data.
### b. calculate_peak_timestamps
"calculate_peak_timestamps" function detects the position i.e. timestamps for each peak.
### c. convert_to_df
"covert_to_df" function add the values of peak_find and their respective positions in a dataframe.
### d. save_peaks_to_csv
"save_peaks_to_csv" function store above created df into a csv file.
### plot_peaks
"plot_peaks" function plots the peaks over the data

## peaks_detect.py
This is the main python file that is used to identify peaks for the data "milk_production.csv".

## Plot showing peaks for "milk_production.csv" with a window size of 1

 

