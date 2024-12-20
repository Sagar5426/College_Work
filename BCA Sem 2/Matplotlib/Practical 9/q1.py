
# write program to plot two lines with legends, different width,
# different colours, axis labels, and a title of the plot.

import matplotlib.pyplot as plt

# Data for the lines
x = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 11]
y2 = [1, 4, 6, 8, 10]
# Plot the lines
plt.plot(x, y1, label='Line 1', color='blue', linewidth=2, marker='o')
plt.plot(x, y2, label='Line 2', color='red', linewidth=3, marker='o')
# Add legends
plt.legend()
# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Two Lines Plot')
# Display the plot
plt.show()
