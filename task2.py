import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import math

M_PI_4 = math.pi / 4


def pifagor_tree(x, y, l, angle, n):
    k = 0.8
    x1 = x - l * math.sin(angle)
    y1 = y + l * math.cos(angle)
    plt.plot([x, x1], [y, y1], color="green")
    if n <= 1:
        return
    pifagor_tree(x1, y1, k * l, angle + M_PI_4, n - 1)
    pifagor_tree(x1, y1, k * l, angle - M_PI_4, n - 1)


level = int(input("Level of recursion: "))

pifagor_tree(0, 0, 2, 0, level)
plt.show()
