# -*- coding: utf-8 -*-
"""
Created on Sun Dec 14 11:20:04 2025

@author: dtabo
"""

import pandas as pd
import numpy as np
from scipy import stats

### Problem 4 ###
Pmaj = 0.01
Pmin = 0.99

#Plane 1 OR Plane 2 require major mx (not both)
P1maj = Pmaj*Pmin + Pmin*Pmaj

print(f" Problem 4. Probabiliy that one, not both aircraft will require major maintenance is: {P1maj}")

### Problem 10 ###
#Calculate euclidean distance

u = [25, 350]
v = [53, 420]

E = np.sqrt((v[0]-u[0])**2+(v[1]-u[1])**2)

print(f"Problem 10. The Euclidean Distance is: {E}")

### Problem 13 ###

CE = 0.75
TS = 250
LR = 1.875
ST = CE/LR
TF = int(ST*TS)

print(f"Problem 13. {TF} Transactions support the consequent")

### Problem 17 ###

n = 10
xbar = 15 
s = 9
Conf = 0.95

# deg of freedom/ std error / t-crit
df = n-1
SE = s/np.sqrt(n)
alpha = 1-Conf
t_crit = stats.t.ppf(1-(alpha/2),df)

# margin of error and CI
MoE = t_crit*SE
CI_low = float(xbar - MoE)
CI_high = float (xbar + MoE)

print(f"The 95% confidence interval for the true mean number of pushups that can be done is: {CI_low},{ CI_high}")

### Problem 18 ###

mu0 = 45
n = 25
xb = 43.118
s = 5.5
alpha = 0.025

# t-test for normal pop/unknown variance. left tailed since Ha <45
# standard error/ test statistic / df
SE = s/np.sqrt(n)
t_test = (xb-mu0)/SE
df = n-1 
# From t-table
t_left = stats.t.ppf(alpha, df)

#reject H0 if t<= t_alpha,df
print(f"Problem 18. (t_test) {t_test} > (t_0.025,24) {t_left}, therefore we do not reject the null hypothesis.") 
print(f"With a 5.5 hour std deviation, this may be due to infamiliarity with the new procedure.")
print(f"I would recommend additional sampling and testing before switching to the new procedure.")


### Problem 25 ###
L = 2
H = 12 
E = (L+H)/2

print(f"Problem 25. E(X), the expected value of the distribution is: {E}")