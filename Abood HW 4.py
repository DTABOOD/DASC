# -*- coding: utf-8 -*-
"""
Created on Mon Dec  1 00:18:33 2025

@author: dtabo
"""


#1. Partition the Data (70/30 split, random_state=42)
print(f"Problem 1")


import pandas as pd
import numpy as np

# Load the mtcars dataset
data = pd.read_csv('mtcars.csv')

# Set random seed for reproducibility
np.random.seed(42)

# Shuffle the data
shuffled = data.sample(frac=1, random_state=42).reset_index(drop=True)

# Calculate split index
split_idx = int(0.7 * len(shuffled))

# Partition the data
train_data = shuffled.iloc[:split_idx]
test_data = shuffled.iloc[split_idx:]

# Optional: Check the sizes
print(f"Training set size: {len(train_data)}")
print(f"Test set size: {len(test_data)}")

#Visualy verify proper partitioning


#2. Fit 10 Simple Linear Regression Models (mpg vs. each predictor) 
print(f"Problem 2")
# Load the mtcars dataset
data = pd.read_csv('mtcars.csv')

# Partition the data (assuming you already did this)
train_data = data.sample(frac=0.7, random_state=42)
# test_data = data.drop(train_data.index)  # Not needed for this step

predictors = [col for col in data.columns if col != 'mpg']

results = []

for predictor in predictors:
    x = train_data[predictor].values
    y = train_data['mpg'].values

    # Calculate means
    x_mean = np.mean(x)
    y_mean = np.mean(y)

    # Calculate slope (β1) and intercept (β0)
    numerator = np.sum((x - x_mean) * (y - y_mean))
    denominator = np.sum((x - x_mean) ** 2)
    beta_1 = numerator / denominator
    beta_0 = y_mean - beta_1 * x_mean

    # Calculate R-squared
    y_pred = beta_0 + beta_1 * x
    ss_total = np.sum((y - y_mean) ** 2)
    ss_res = np.sum((y - y_pred) ** 2)
    r_squared = 1 - (ss_res / ss_total)

    results.append({
        'Predictor': predictor,
        'Intercept': beta_0,
        'Slope': beta_1,
        'R-squared': r_squared
    })

# Convert results to DataFrame for easy viewing
results_df = pd.DataFrame(results)
print(results_df)



#3. Select Best Model (Highest R² and significant t-stat)

print(f"Problem 3")

# Let's assume results_df looks like this:
# results_df = pd.DataFrame([
#     {'Predictor': 'cyl', 'Intercept': ..., 'Slope': ..., 'R-squared': ...},
#     {'Predictor': 'disp', 'Intercept': ..., 'Slope': ..., 'R-squared': ...},
#     ...
# ])

# Find the row with the highest R-squared value
best_model_row = results_df.loc[results_df['R-squared'].idxmax()]

# Extract the predictor name
best_predictor = best_model_row['Predictor']

# Extract the intercept and slope
best_intercept = best_model_row['Intercept']
best_slope = best_model_row['Slope']

# Print out the results in a human-readable way
print("Best simple linear regression model:")
print(f"Predictor: {best_predictor}")
print(f"Equation: mpg = {best_intercept:.4f} + {best_slope:.4f} * {best_predictor}")
print(f"R-squared: {best_model_row['R-squared']:.4f}")

# Interpretation
print(f"This means that '{best_predictor}' is the variable most strongly related to mpg in your training data.")
print(f"For each unit increase in {best_predictor}, mpg changes by {best_slope:.4f} units (according to this model).")


#4. Write Equation for Best Model and Interpret
print(f"Problem 4")

best_predictor = best_model_row['Predictor']
best_intercept = best_model_row['Intercept']
best_slope = best_model_row['Slope']

# Write out the equation
print(f"Equation: mpg = {best_intercept:.4f} + {best_slope:.4f} * {best_predictor}")

# Interpretation
print(f"For each unit increase in {best_predictor}, mpg changes by {best_slope:.4f} units.")


#5. Multiple Linear Regression (mpg vs. all predictors)
print(f"Problem 5")

# Prepare the data
X = train_data[predictors].values  # All predictors
y = train_data['mpg'].values

# Add a column of ones for the intercept
X_with_intercept = np.column_stack((np.ones(X.shape[0]), X))

# Fit the model using least squares
coeffs, residuals, rank, s = np.linalg.lstsq(X_with_intercept, y, rcond=None)

# Intercept is coeffs[0], the rest are for each predictor
intercept = coeffs[0]
slopes = coeffs[1:]

# Print the equation
equation = f"mpg = {intercept:.4f}"
for i, predictor in enumerate(predictors):
    equation += f" + {slopes[i]:.4f}*{predictor}"
print("Multiple regression equation:")
print(equation)


y_pred = X_with_intercept @ coeffs
ss_total = np.sum((y - np.mean(y)) ** 2)
ss_res = np.sum((y - y_pred) ** 2)
r_squared_multi = 1 - (ss_res / ss_total)



#6. Compare Multiple Regression to Simple Models
print(f"Problem 6")


print(f"Multiple regression R-squared: {r_squared_multi:.4f}")
print(f"Best simple model R-squared: {best_model_row['R-squared']:.4f}")
print(f"Range of simple model R-squared: {results_df['R-squared'].min():.4f} to {results_df['R-squared'].max():.4f}")

# If the multiple regression R² is much higher, it means using all predictors together explains mpg better than any single predictor.
# If not, it means one variable alone is almost as good as all combined.

#7. Extra Credit: Parsimonious Model (Backward Elimination)
print(f"Problem 7:Extra Credit")

# Start with all predictors
selected_predictors = predictors.copy()
best_r2 = r_squared_multi

for predictor in predictors:
    temp_predictors = [p for p in selected_predictors if p != predictor]
    X_temp = train_data[temp_predictors].values
    X_temp_with_intercept = np.column_stack((np.ones(X_temp.shape[0]), X_temp))
    coeffs_temp, _, _, _ = np.linalg.lstsq(X_temp_with_intercept, y, rcond=None)
    y_pred_temp = X_temp_with_intercept @ coeffs_temp
    ss_res_temp = np.sum((y - y_pred_temp) ** 2)
    r2_temp = 1 - (ss_res_temp / ss_total)
    print(f"R-squared without {predictor}: {r2_temp:.4f}")
    # If R² drops a lot, keep the predictor
    if r2_temp < best_r2 - 0.02:  # Threshold for "significant" drop
        print(f"Keeping {predictor}")
    else:
        selected_predictors.remove(predictor)
        best_r2 = r2_temp

print("Selected predictors for parsimonious model:", selected_predictors)
