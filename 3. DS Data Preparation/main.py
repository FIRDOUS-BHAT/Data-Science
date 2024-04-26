# This Python code snippet is using the pandas library to read data from a CSV file named "data.csv"
# into a DataFrame object named `health_data`. Here's a breakdown of each line:
import pandas as pd

health_data = pd.read_csv("data.csv", header=0, sep=",")

print(health_data)


# Remove Blank Rows
# We see that the non-numeric values(9 000 and AF) are in the same rows with missing values.

# Solution: We can remove the rows with missing observations to fix this problem.

# When we load a data set using Pandas, all blank cells are automatically converted into "NaN" values.

# So, removing the NaN cells gives us a clean data set that can be analyzed.

# We can use the dropna() function to remove the NaNs. axis = 0 means that we want to remove all rows that have a NaN value:

health_data.dropna(axis=0, inplace=True)

print(health_data)

# Data Types

# We can use the info() function to list the data types within our data set:
print(health_data.info())


# Analyze the Data
# When we have cleaned the data set, we can start analyzing the data.

# We can use the describe() function in Python to summarize data:


print(health_data.describe())
