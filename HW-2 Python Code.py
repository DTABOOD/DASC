# -*- coding: utf-8 -*-
"""
Created on Mon Nov  3 01:26:48 2025

@author: dtabo
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Oct 26 11:21:05 2025
@author: MD's PC
"""
####### Import Libraries #######
#import pdfkit
from jinja2 import Environment, FileSystemLoader
####### Import Libraries #######
import statistics as st
import numpy as np
import seaborn as sbimport
import matplotlib
import matplotlib.pyplot as plt
import seaborn as snsimport
import random
import pandas as pd
import scipy as space
from itertools import product
from collections import Counter
from fractions import Fraction
from jinja2 import Environment, FileSystemLoader
import os
#import pdfkit
# Define colors
C = ["R", "G", "B"]
#a. Generate sample space as ordered pairs (C1, C2)
#SS = RXGXB = 3X3
SS = [(c1, c2) for c1 in C for c2 in C]
#b. Calc probability for each outcome
#P((c1,c2)) = P(c1)XP(c2)
probability_each = 1 / len(SS)
# Print results
print("Sample Space:", SS)
print("b. ")
print("Total number of outcomes:", len(SS))
print("Probability of each outcome:", probability_each)
#Same experiment, Order of marble color selection doesn't matter:
# (R, B) = (B, R)
#c. What is the sample space when order doesn't matter?
# Generate all ordered pairs (C1, C2)

ordered_pairs = list(product(C, repeat=2))
# Convert each ordered pair to an unordered pair (so (R,G) and (G,R) are treated the same)
unordered_pairs = [tuple(sorted(pair)) for pair in ordered_pairs]
# Count how many times each unordered pair appears
counts = Counter(unordered_pairs)
# Total number of ordered outcomes
total = len(ordered_pairs)
#Print Results
print ("c. Unordered Sample Space and Probabilities :\n")
for outcome, count in counts.items():
 prob_fraction = Fraction(count, total) # Convert to fraction
 prob_decimal = count / total
 print(f"{outcome}: {prob_fraction} ({prob_decimal:.3f})")
#Problem #2
# Define the sample space
cards = list(range(1, 11))
# Cards 1-10
E = [10] # Event E: card is 10
F = [5, 6, 7, 8, 9, 10] # Event F: card is at least 5
# Calculate probabilities
P_E = len(E) / len(cards) # P(E)
P_F = len(F) / len(cards) # P(F)
P_E_and_F = len(set(E) & set(F)) / len(cards) # P(E ∩ F)
# Conditional probability P(E | F)
P_E_given_F = P_E_and_F / P_F
# Display results
print("P(E) =", P_E)
print("P(F) =", P_F)
print("P(E ∩ F) =", P_E_and_F)
print("P(E | F) =", P_E_given_F)
#Problem 4
# Load dataset
file_path = "Logan.csv" # make sure this file is in the same folder or use full path
df = pd.read_csv(file_path)
# Define task columns (exclude City)
tasks = df.columns[1:]
plt.style.use('seaborn-colorblind')
# -------------------------------------------------------
# (a) Stacked Bar Chart
# -------------------------------------------------------
df.set_index('City')[tasks].plot(kind='barh', stacked=True, figsize=(10, 6))


plt.title("Manager Time Allocation by Store Location (Stacked Bar)")
plt.xlabel("Percentage of Time")
plt.ylabel("Store Location")
plt.legend(title="Task", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
# -------------------------------------------------------
# (b) Clustered Bar Chart
# -------------------------------------------------------
df.set_index('City')[tasks].plot(kind='barh', stacked=False, figsize=(10, 6))
plt.title("Manager Time Allocation by Store Location (Clustered Bar)")
plt.xlabel("Percentage of Time")
plt.ylabel("Store Location")
plt.legend(title="Task", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
# -------------------------------------------------------
# (c) Individual Bar Charts for each City
# -------------------------------------------------------
for _, row in df.iterrows():
 plt.figure(figsize=(6, 4))
 plt.bar(row.index[1:], row.values[1:], color=['#1f77b4','#ff7f0e','#2ca02c','#d62728'])
 plt.title(f"Manager Time Allocation - {row['City']}")
 plt.ylabel("Percentage of Time")
 plt.xticks(rotation=45, ha='right')
 plt.ylim(0, 1)
 plt.tight_layout()
 plt.show()
# -------------------------------------------------------
# (d) Heatmap-style Chart (Using Matplotlib Only)
# -------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 5))
data = df.set_index('City')[tasks].values
im = ax.imshow(data, cmap='YlGnBu')
# Add labels
ax.set_xticks(np.arange(len(tasks)))
ax.set_yticks(np.arange(len(df['City'])))
ax.set_xticklabels(tasks, rotation=45, ha="right")
ax.set_yticklabels(df['City'])
plt.title("Heatmap of Manager Time Allocation by Task and Store Location")
# Annotate cells
for i in range(len(df['City'])):
 for j in range(len(tasks)):
     ax.text(j, i, f"{data[i, j]:.2f}", ha="center", va="center", color="black")
# Add colorbar
cbar = plt.colorbar(im)
cbar.set_label('Proportion of Time')
plt.tight_layout()
plt.show()
# -------------------------------------------------------
# (e) Analysis of Similarities and Differences
# -------------------------------------------------------
print("\n--- Inferences ---")
print("• Most managers spend significant time on Customer Interaction and Attending Required Meetings.")
print("• Boise and Bend focus heavily on Customer Interaction.")
print("• Portland devotes the most time to Attending Required Meetings.")
print("• Missoula shows higher Idle time, possibly due to lower workload or inefficiencies.")
print("• Seattle’s distribution appears relatively balanced across tasks.")
#Exra Credit
#Develop and execute a simulation of the marble-draw scenarios described in Question 1.
#• Present the code used to simulate the scenario.
#• Provide the results of the simulation and the estimated sample space probabilities.
#• State whether the simulation results match your answers to both parts of Question 1 and explain why or why not.