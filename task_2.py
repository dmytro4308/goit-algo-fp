import matplotlib.pyplot as plt
import numpy as np

def draw_tree(x, y, angle, length, level, ax):
    if level == 0:
        return

    # calculate end coordinates
    x_end = x + length * np.cos(angle)
    y_end = y + length * np.sin(angle)

    # draw branch
    ax.plot([x, x_end], [y, y_end], color="green")

    # draw lesser branches
    new_length = length * 0.7
    draw_tree(x_end, y_end, angle + np.pi / 4, new_length, level - 1, ax)
    draw_tree(x_end, y_end, angle - np.pi / 4, new_length, level - 1, ax)

def pythagoras_tree(level):
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.axis('off')
    draw_tree(x=0, y=0, angle=np.pi/2, length=100, level=level, ax=ax)
    plt.title(f"Pythagoras tree: recursion level {level}")
    plt.show()

if __name__ == "__main__":
    try:
        level = int(input("Enter recursion level (e.g, 5): "))
        pythagoras_tree(level)
    except ValueError:
        print("Please enter an integer.")
