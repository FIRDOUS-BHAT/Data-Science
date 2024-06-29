# Data Science Statistics - Variance
# Variance is a measure of how spread out the numbers in a data set are.
# Variance is the average of the squared differences from the Mean.
# To calculate the variance follow these steps:
# 1. Work out the Mean (the simple average of the numbers)
# 2. Then for each number: subtract the Mean and square the result (the squared difference).
# 3. Then work out the average of those squared differences.
# Example: To calculate the variance of [1, 2, 3, 4, 5] do:
# 1. The Mean is (1+2+3+4+5)/5 = 3
# 2. Subtract the Mean and square the result:
#   For 1: (1-3)2 = (-2)2 = 4
#   For 2: (2-3)2 = (-1)2 = 1
#   For 3: (3-3)2 = (0)2 = 0
#   For 4: (4-3)2 = (1)2 = 1
#   For 5: (5-3)2 = (2)2 = 4
# 3. The variance is the average of these squared differences: (4+1+0+1+4)/5 = 2
# So the Variance is 2
# Variance is often shown as σ2, so the variance of [1, 2, 3, 4, 5] can be written as σ2 = 2
# Variance is the square of the Standard Deviation
# Standard Deviation is the square root of Variance


# Pythonic way to calculate Variance
# We can use the var() function from Numpy to find the variance (remember that we now use the first data set with 10 observations):
import pandas as pd
import numpy as np
speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
x = np.var(speed)
print(x)

# The result is 92.21, which is the same as we calculated in the example above.

# Example 2: Calculate the variance of the data set in the data.csv file


health_data = pd.read_csv("data.csv", header=0, sep=",")

var = np.var(health_data)

print(var)
