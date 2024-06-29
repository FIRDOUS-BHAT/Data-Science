# Data Science Statistics - Correlation
# Correlation is a statistical measure that describes the association between random variables.
# In other words, it is a measure of how things are related.
# The most common measure of correlation in stats is the Pearson Correlation.
# The Pearson Correlation evaluates the linear relationship between two continuous variables.
# A relationship is linear when a change in one variable is associated with a proportional change in the other variable.
# The formula to find the correlation between two variables is:


# Correlation Coefficient
# The correlation coefficient measures the relationship between two variables.

# The correlation coefficient can never be less than - 1 or higher than 1.

# 1 = there is a perfect linear relationship between the variables(like Average_Pulse against Calorie_Burnage)
# 0 = there is no linear relationship between the variables
# -1 = there is a perfect negative linear relationship between the variables(e.g. Less hours worked, leads to higher calorie burnage during a training session)


# Three lines to make our compiler able to draw:
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import sys
import matplotlib

# `matplotlib.use('Agg')` is a command in Matplotlib that sets the backend to 'Agg', which is a
# non-interactive backend. This backend is particularly useful when you want to save plots to a file
# without displaying them interactively. By setting the backend to 'Agg', Matplotlib will create the
# plots in memory and save them to a file without showing them on the screen. This is commonly used in
# scenarios where you want to generate plots in a non-interactive environment, such as when running
# scripts in a server environment or when saving plots automatically without user interaction.
matplotlib.use('Agg')

# Read the data from file
health_data = pd.read_csv("data.csv", header=0, sep=",")

# Create a scatter plot of Average_Pulse vs Calorie_Burnage
# The kind='scatter' parameter is not necessary, but it makes the code more explicit
health_data.plot(x='Average_Pulse', y='Calorie_Burnage', kind='scatter')

# Show the plot
plt.show()

# Two lines to make our compiler able to draw:
# Save the plot to stdout buffer and flush the buffer
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()


# Correlation Matrix in Python
# We can use the corr() function in Python to create a correlation matrix. We also use the round() function to round the output to two decimals:


full_health_data = pd.read_csv("data.csv", header=0, sep=",")

Corr_Matrix = round(full_health_data.corr(), 2)

print(Corr_Matrix)


# We can use a Heatmap to Visualize the Correlation Between Variables:

# Use Seaborn to Create a Heatmap
# We can use the Seaborn library to create a correlation heat map(Seaborn is a visualization library based on matplotlib):


full_health_data = pd.read_csv("dataset.csv", header=0, sep=",")
correlation_full_health = full_health_data.corr()

axis_corr = sns.heatmap(
    correlation_full_health,
    vmin=-1, vmax=1, center=0,
    cmap=sns.diverging_palette(50, 500, n=500),
    square=True
)

plt.show()


# Example Explained:
# Import the library seaborn as sns.
# Use the full_health_data set.
# Use sns.heatmap() to tell Python that we want a heatmap to visualize the correlation matrix.
# Use the correlation matrix. Define the maximal and minimal values of the heatmap. Define that 0 is the center.
# Define the colors with sns.diverging_palette. n = 500 means that we want 500 types of color in the same color palette.
# square = True means that we want to see squares.


# correlation vs casuality

# Three lines to make our compiler able to draw:
matplotlib.use('Agg')


# Plot the number of drowning accidents against the number of ice cream sales
# in a beach. This will give us an idea of the correlation between these
# two variables.
# The comments and docstrings will help us understand the code better.

Drowning_Accident = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200]
Ice_Cream_Sale = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200]

# Create a Pandas DataFrame using a dictionary
Drowning = {"Drowning_Accident": Drowning_Accident,
            "Ice_Cream_Sale": Ice_Cream_Sale}
Drowning = pd.DataFrame(data=Drowning)

# Use the DataFrame.plot() method to create a scatter plot of
# Ice_Cream_Sale against Drowning_Accident.
# The kind='scatter' parameter is not necessary, but it makes the code
# more explicit.
Drowning.plot(x="Ice_Cream_Sale", y="Drowning_Accident", kind="scatter")

# Show the plot.
plt.show()

# Calculate the correlation between Ice_Cream_Sale and
# Drowning_Accident. The corr() method returns a correlation coefficient.
correlation_beach = Drowning.corr()

# Print the correlation coefficient.
print(correlation_beach)

# Two lines to make our compiler able to draw:
# Save the plot to stdout buffer and flush the buffer
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
