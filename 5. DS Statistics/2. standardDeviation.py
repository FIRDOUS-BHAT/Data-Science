# Standard deviation is a number that describes how spread out the observations are.

# We can use the std() function from Numpy to find the standard deviation of a variable:

import numpy as np
import pandas as pd

full_health_data = pd.read_csv("data.csv", header=0, sep=",")

std = np.std(full_health_data)
print(std)

# Coefficient of Variation
# The coefficient of variation is used to get an idea of how large the standard deviation is .

# Mathematically, the coefficient of variation is defined as:

# Coefficient of Variation = Standard Deviation / Mean
# We can do this in Python if we proceed with the following code:

# Example

cv = np.std(full_health_data) / np.mean(full_health_data)
print(cv)
