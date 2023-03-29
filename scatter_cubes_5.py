import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [y**3 for y in x_values]

fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c='green', s=25)

# Set title and axis labels
ax.set_title('Cube numbers', fontsize=18)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Cube of value', fontsize=14)

plt.show()