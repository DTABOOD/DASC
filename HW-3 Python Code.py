# -*- coding: utf-8 -*-
"""
Created on Mon Nov  3 01:29:04 2025

@author: dtabo
"""

#Homework #3

####### Import Libraries #######

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Load the data
df = pd.read_csv('Advertising.csv')

#Problem #1

# Set sample size N (e.g., N = 30)
N = 30

# Generate random sample without replacement
sample = df['Newspaper'].sample(n=N, replace=False, random_state=42)
print(sample)

# Generate sample
sample_30 = df['Newspaper'].sample(n=30, replace=False, random_state=42)

# Create histogram
plt.hist(sample_30, bins=10, edgecolor='black')
plt.title('Histogram of Newspaper Sample (N=30)')
plt.xlabel('Newspaper Budget (thousands of dollars)')
plt.ylabel('Frequency')
plt.show()


# Manually compute mean and sample variance
mean_manual = sum(sample_30) / len(sample_30)
variance_manual = sum((x - mean_manual) ** 2 for x in sample_30) / (len(sample_30) - 1)

# Using built-in functions
mean_func = np.mean(sample_30)
variance_func = np.var(sample_30, ddof=1)

print(f"Manual Mean: {mean_manual}, Manual Variance: {variance_manual}")
print(f"Function Mean: {mean_func}, Function Variance: {variance_func}")

n = len(sample_30)
mean = mean_manual
std = np.sqrt(variance_manual)
conf_int = stats.t.interval(0.95, df=n-1, loc=mean, scale=std/np.sqrt(n))
print(f"95% Confidence Interval: {conf_int}")


mu_0 = 30.55
W = (mean - mu_0) / (std / np.sqrt(n))
p_value = 2 * (1 - stats.t.cdf(abs(W), df=n-1))
print(f"Test Statistic W: {W}")
print(f"P-value: {p_value}")
if p_value < 0.05:
    print("Reject H0: The mean is significantly different from 30.55.")
else:
    print("Fail to reject H0: No significant difference from 30.55.")



results = []
for i in range(3):
    sample = df['Newspaper'].sample(n=30, replace=False)
    mean = np.mean(sample)
    variance = np.var(sample, ddof=1)
    std = np.sqrt(variance)
    conf_int = stats.t.interval(0.95, df=29, loc=mean, scale=std/np.sqrt(30))
    W = (mean - mu_0) / (std / np.sqrt(30))
    p_value = 2 * (1 - stats.t.cdf(abs(W), df=29))
    conclusion = "Reject H0" if p_value < 0.05 else "Fail to reject H0"
    results.append({
        'Sample Mean': mean,
        'Sample Variance': variance,
        'Confidence Interval': conf_int,
        'Test Statistic W': W,
        'Conclusion': conclusion
    })
for i, res in enumerate(results, 1):
    print(f"Iteration {i}: {res}")


results_100 = []
for i in range(3):
    sample = df['Newspaper'].sample(n=100, replace=False)
    mean = np.mean(sample)
    variance = np.var(sample, ddof=1)
    std = np.sqrt(variance)
    conf_int = stats.t.interval(0.95, df=99, loc=mean, scale=std/np.sqrt(100))
    W = (mean - mu_0) / (std / np.sqrt(100))
    p_value = 2 * (1 - stats.t.cdf(abs(W), df=99))
    conclusion = "Reject H0" if p_value < 0.05 else "Fail to reject H0"
    results_100.append({
        'Sample Mean': mean,
        'Sample Variance': variance,
        'Confidence Interval': conf_int,
        'Test Statistic W': W,
        'Conclusion': conclusion
    })
for i, res in enumerate(results_100, 1):
    print(f"Iteration {i}: {res}")

#EXTRA CREDIT

# Load the data
df = pd.read_csv('Advertising.csv')

# Generate a sample
N = 30
sample = df['Newspaper'].sample(n=N, replace=False, random_state=42)

# Compute sample mean and standard deviation
sample_mean = np.mean(sample)
sample_std = np.std(sample, ddof=1)

# Hypothesized mean
mu_0 = 30.55

# Compute test statistic W
W = (sample_mean - mu_0) / (sample_std / np.sqrt(N))

# Compute 95% confidence interval for the mean
alpha = 0.05
t_crit = stats.t.ppf(1 - alpha/2, df=N-1)
conf_int_lower = sample_mean - t_crit * (sample_std / np.sqrt(N))
conf_int_upper = sample_mean + t_crit * (sample_std / np.sqrt(N))

# Print results
print(f"Sample Mean: {sample_mean:.2f}")
print(f"Sample Std Dev: {sample_std:.2f}")
print(f"Test Statistic W: {W:.2f}")
print(f"95% Confidence Interval: ({conf_int_lower:.2f}, {conf_int_upper:.2f})")

# Check if mu_0 is inside the confidence interval
if conf_int_lower <= mu_0 <= conf_int_upper:
    print("mu_0 is inside the confidence interval: Fail to reject H0")
else:
    print("mu_0 is outside the confidence interval: Reject H0")

# Compute p-value for hypothesis test
p_value = 2 * (1 - stats.t.cdf(abs(W), df=N-1))
print(f"P-value: {p_value:.4f}")

