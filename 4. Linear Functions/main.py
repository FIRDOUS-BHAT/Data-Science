# Linear Functions
# In mathematics a function is used to relate one variable to another variable.


# A linear function has one independent variable(x) and one dependent variable(y), and has the following form:

"""
y = f(x) = ax + b

"""

# Three lines to make our compiler able to draw:
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sys
import matplotlib
matplotlib.use('Agg')


health_data = pd.read_csv("data.csv", header=0, sep=",")

health_data.plot(x='Average_Pulse', y='Calorie_Burnage', kind='line')
plt.ylim(ymin=0)
plt.xlim(xmin=0)

plt.show()

# Two lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()


# Explanation:

# f(x) = the output(the dependant variable)
# x = the input(the independant variable)
# a = slope = is the coefficient of the independent variable. It gives the rate of change of the dependent variable
# b = intercept = is the value of the dependent variable when x = 0. It is also the point where the diagonal line crosses the vertical axis.


# Example Explained
# Import the pyplot module of the matplotlib library
# Plot the data from Average_Pulse against Calorie_Burnage
# kind = 'line' tells us which type of plot we want. Here, we want to have a straight line
# plt.ylim() and plt.xlim() tells us what value we want the axis to start on. Here, we want the axis to begin from zero
# plt.show() shows us the output


# Slope and Intercept

# Now we will explain how we found the slope and intercept of our function:

# f(x) = 2x + 80

# The image below points to the Slope - which indicates how steep the line is , and the Intercept - which is the value of y, when x = 0 (the point where the diagonal line crosses the vertical axis). The red line is the continuation of the blue line from previous page.


# Find the Slope and Intercept Using Python
# The np.polyfit() function returns the slope and intercept.

# If we proceed with the following code, we can both get the slope and intercept from the function.


health_data = pd.read_csv("data.csv", header=0, sep=",")

x = health_data["Average_Pulse"]
y = health_data["Calorie_Burnage"]
slope_intercept = np.polyfit(x, y, 1)

print(slope_intercept)
