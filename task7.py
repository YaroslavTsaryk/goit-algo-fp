import numpy as np


def monte_carlo_dice(num_points):
    res = {x: 0 for x in range(2, 13)}
    x = np.random.randint(1, 7, num_points)
    y = np.random.randint(1, 7, num_points)
    for i in range(num_points):
        res[x[i] + y[i]] += 1

    for i in range(2, 13):
        print(f"Sum {i}:\t{res[i]}\t{res[i]/num_points*100}")


monte_carlo_dice(1_000_000)
