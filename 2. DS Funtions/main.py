# commonly used functions when working with Data Science: max(), min(), and mean().

# The Python max() function is used to find the highest value in an array.


import numpy as np
Average_pulse_max = max(80, 85, 90, 95, 100, 105, 110, 115, 120, 125)

print(Average_pulse_max)


# The Python min() function is used to find the lowest value in an array.

Average_pulse_min = min(80, 85, 90, 95, 100, 105, 110, 115, 120, 125)

print(Average_pulse_min)


# The NumPy mean() function is used to find the average value of an array.


Calorie_burnage = [240, 250, 260, 270, 280, 290, 300, 310, 320, 330]

Average_calorie_burnage = np.mean(Calorie_burnage)

print(Average_calorie_burnage)
