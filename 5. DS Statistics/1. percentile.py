# Percentiles are used in statistics to give you a number that describes the value that a given percent of the values are lower than.


# Task: Find the 10 % percentile for Max_Pulse

import numpy as np
import pandas as pd



full_health_data = pd.read_csv("data.csv", header=0, sep=",")

Max_Pulse = full_health_data["Max_Pulse"]
percentile10 = np.percentile(Max_Pulse, 10)
print(percentile10)
