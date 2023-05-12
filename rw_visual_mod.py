# Modify visualisation to simulate pollen grain on surface of a drop of water

import matplotlib.pyplot as plt

from random_walk_mod import RandomWalk

# Keep making new walk, as long as the program is active
while True:
    # Make a random walk
    rw = RandomWalk(5000)
    rw.fill_walk()

    # Plot the points in the walk
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9))
    point_numbers = range(rw.num_points)
    ax.plot(rw.x_values, rw.y_values, linewidth=8)

    # Remove the axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Create another walk? (y/n): ")
    if keep_running == 'n':
        break