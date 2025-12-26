# -*- coding: utf-8 -*-
"""
Created on Sun Nov 16 14:43:16 2025

@author: dtabo
"""

import pandas as pd
import numpy as np
from scipy import stats

#PROBLEM 22
r = 2
y = 4
p = 5
tb = r+y+p

R1 = r/tb
P2 = p/tb

prob_R1P2 = R1*P2

print(prob_R1P2)


#PROBLEM 23

# Load the dataset
df = pd.read_csv("Advertising.csv")

# Extract the 'Radio' column
radio_data = df['Radio'].dropna()
n = len(radio_data)
mean_radio = np.mean(radio_data)
var_radio = np.var(radio_data, ddof=1)  # sample variance
print(f"Number of observations: {n}")
print(f"Sample mean of Radio: {mean_radio:.4f}")
print(f"Sample variance of Radio: {var_radio:.4f}\n")

# 95% confidence interval for the mean
alpha = 0.05
t_critical = stats.t.ppf(1 - alpha/2, df=n-1)
std_err = np.std(radio_data, ddof=1) / np.sqrt(n)
mean_ci_lower = mean_radio - t_critical * std_err
mean_ci_upper = mean_radio + t_critical * std_err
print(f"95% Confidence Interval for Mean: ({mean_ci_lower:.4f}, {mean_ci_upper:.4f})")

# 95% confidence interval for the variance using Chi-square distribution
chi2_lower = stats.chi2.ppf(alpha/2, df=n-1)
chi2_upper = stats.chi2.ppf(1 - alpha/2, df=n-1)
var_ci_lower = (n-1) * var_radio / chi2_upper
var_ci_upper = (n-1) * var_radio / chi2_lower
print(f"95% Confidence Interval for Variance: ({var_ci_lower:.4f}, {var_ci_upper:.4f})")
