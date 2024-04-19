import numpy as np
import matplotlib.pyplot as plt

# Data for the plot
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

# Configure the line plot
plt.subplot(2, 1, 1)  # Divide the drawing area into 2 rows and 1 column
plt.plot(x, y, 'ro-', label='Data')  # 'ro-' indicates red points connected by lines
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Line Plot")
plt.legend()

# Configure the scatter plot with regression line
plt.subplot(2, 1, 2)  # Second row of the drawing area
plt.scatter(x, y, color='blue', label='Data')

# Configure the parameters for the regression line
slope = 1.2
intercept = 0.5

# Generate data points for the regression line
x_reg = np.linspace(min(x), max(x), 100)
y_reg = slope * x_reg + intercept

plt.plot(x_reg, y_reg, color='red', label='Regression Line')
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Scatter Plot with Regression Line")
plt.legend()

# Display the plots
plt.tight_layout()  # Adjust the spacing of the plots
plt.show()
