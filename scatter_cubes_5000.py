import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

fig, ax = plt.subplots()

# Set title and axis labels and tick marks
ax.set_title("Cube numbers up to 5000^3", fontsize=18)
ax.set_xlabel("Value", fontsize=12)
ax.set_ylabel("Cube of value", fontsize=12)
ax.tick_params(axis='both', which='major', labelsize=6)
ax.ticklabel_format(style='plain')

ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=10)

plt.show()