# -*- coding: utf-8 -*-
"""
Created on Mon Nov  3 01:36:28 2025

@author: dtabo
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Oct 5 13:07:57 2025
@author: MD's PC
"""
import statistics as st
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
import random
import pandas as pd
import scipy as sp
#PROBLEM #1
#import the commute times file
ct = pd.read_csv('CommuteTimes.csv', delimiter=',', header = 0)
#pull list of times from file
times = ct["Time (minutes)"].tolist()
print(f"Problem #1: Commute Times")
#find the mean for the commute times
mean = st.mean(times)
print(f"1a. Mean: {mean}")
#find the median for the commute times
median = st.median(times)
print(f"1b. Median: {median}")
#find the mode for the commute times
mode = st.mode(times)
print(f"1c. Mode: {mode}")
#find population variance and population standard deviation
pop_var = st.pvariance(times)
print(f"1d. Population Variance: {pop_var}")
pop_std_dev = st.pstdev(times)
print(f"1d. Standard Deviation: {pop_std_dev}")
#find the third quartile for commute times
third_quartile = np.quantile(times, 0.75)
print(f"1e. Third Quartile (Q3): {third_quartile}")
#PROBLEM #2
#import the jobless rate file
joblessrate = pd.read_csv('JoblessRate.csv', delimiter=',', header = 0)#pull list of jobless rates and delinquent loans
jr = joblessrate["Jobless_rate"].tolist()
dl = joblessrate["Delinquent_Loans"].tolist()

cities = joblessrate["Metro_Area"].tolist()
print(f"Problem #2: Jobless Rate")
#calculate the means
mean_jr = st.mean(jr)
mean_dl = st.mean(dl)
print(f"2ai. Jobless Rate % Mean: {mean_jr}")
print(f"2aii. Delinquent Loan % Mean: {mean_dl}")
#calculate the medians
median_jr = st.median(jr)
median_dl = st.median(dl)
print(f"2bi. Jobless Rate % Median: {median_jr}")
print(f"2bii. Delinquent Loan % Median: {median_dl}")
#Calculate the sample variance and standard deviations
sv_jr = st.variance(jr)
sv_dl = st.variance(dl)
std_dev_jr = st.pstdev(jr)
std_dev_dl = st.pstdev(dl)
print(f"2ci.")
print(f"Jobless Rate sample variance: {sv_jr}")
print(f"Jobless Rate standard deviation: {std_dev_jr}")
print(f"2cii.")
print(f"Delinquent Loan sample variance: {sv_dl}")
print(f"Delinquent Loan standard deviation: {std_dev_dl}")
#Find the pearson correlation coefficient between jobless rate and delinquent loan#r = (Σ(xi - XŊ)(yi - Ȳ)) / (√[Σ(xi - XŊ)² Σ(yi - Ȳ)²])
#Ensure the lists are the same length
if len(jr) != len(dl):
 raise ValueError ("Lists must have the same length")

#Means already calculated
numerator = sum((x-mean_jr)*(y-mean_dl) for x,y in zip(jr,dl))
denominator_1 = sum((x-mean_jr)**2 for x in jr)
denominator_2 = sum((y-mean_dl)**2 for y in dl)
denominator = np.sqrt(denominator_1*denominator_2)
print(f"2d.")
if denominator == 0:
 print(f" 0.0")
print(f"The Pearson correlation coefficient is {numerator/denominator}")#Develop a Histogram to portlay jr and dl distribution
#df.hist(column='col_name')


#Plot Jobless Rate Histogram
# Use Freedman-Diaconis rule to find a good bin width
q25, q75 = np.percentile(jr, [25, 75])
bin_width = 2 * (q75 - q25) * len(jr) ** (-1/3)
bins = round((max(jr) - min(jr)) / bin_width)
print("Freedman–Diaconis number of bins:", bins)
plt.hist(jr, bins=bins, edgecolor='black');
#plt.hist(jr, edgecolor='black') # 'bins' controls the number of bars, 'edgecolor' adds outlines# Add labels and title for clarity
plt.xlabel("Jobless Rate %")
plt.ylabel("Number of Metro Areas")
plt.title("Distribution of Jobless Rate")
# Display the plot
plt.show()
# Plot Delinquent Loan Histogram
# Use Freedman-Diaconis rule to find a good bin width
q25, q75 = np.percentile(dl, [25, 75])
bin_width = 2 * (q75 - q25) * len(dl) ** (-1/3)
bins = round((max(dl) - min(dl)) / bin_width)
print("Freedman–Diaconis number of bins:", bins)
plt.hist(dl, bins=bins, edgecolor='black');
#plt.hist(dl, edgecolor='black') # 'bins' controls the number of bars, 'edgecolor' adds outlines# Add labels and title for clarity
plt.xlabel("Delinquent Loan %")
plt.ylabel("Number of Metro Areas")
plt.title("Distribution of Delinquent Loans")
# Display the plot
plt.show()