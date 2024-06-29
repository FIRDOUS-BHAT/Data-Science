# Linear regression in data science

# Linear regression is a statistical method that models the relationship between
# two variables by fitting a linear equation to observed data. One variable is
# considered to be an independent variable, and the other is considered to be a
# dependent variable. For example, a modeler might want to relate the weights of
# individuals to their heights using a linear regression model. In this case, the
# model would be a linear equation that predicts weight as a function of height.
# In general, a linear regression line has an equation of the form:  y = a + bx
# where  y  is the dependent variable,  x  is the independent variable,  b  is
# the slope of the line, and  a  is the y-intercept. The slope  b
# represents the rate of change in  y  as  x  changes, and the intercept
# a  is the value of  y  when  x = 0 . The goal of linear regression is to
# find the best-fitting line through the data points that minimizes the sum
# of the squared differences between the observed values and the values predicted
# by the model. This method is called the method of least squares.
# The best-fitting line is also known as the regression line.
# The regression line can be used to predict the value of the dependent variable
# for any value of the independent variable within the range of the data.
# Linear regression is widely used in data science and machine learning for modeling
# and predicting continuous variables. It is a simple and powerful tool that can provide
# valuable insights into the relationships between variables in a dataset.
# In this tutorial, we will learn how to perform linear regression in Python using the
# scikit-learn library. We will use a sample dataset to build a linear regression model
# and make predictions based on the model. Let's get started!


import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats


full_health_data = pd.read_csv("data.csv", header=0, sep=",")

x = full_health_data["Average_Pulse"]
y = full_health_data["Calorie_Burnage"]

slope, intercept, r, p, std_err = stats.linregress(x, y)


def myfunc(x):  
    return slope * x + intercept    


mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, slope * x + intercept)
plt.ylim(ymin=0, ymax=2000)
plt.xlim(xmin=0, xmax=200)
plt.xlabel("Average_Pulse")
plt.ylabel("Calorie_Burnage")
plt.show()


# provide more examples of linear regression
# https://scikit-learn.org/stable/auto_examples/linear_model/plot_ols.html#sphx-glr-auto-examples-linear-model-plot-ols-py







