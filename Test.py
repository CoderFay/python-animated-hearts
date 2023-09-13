import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
fig.set_facecolor('black')  
ax.set_aspect('equal')

t = np.linspace(0, 2 * np.pi, 1000)
x = 16 * np.sin(t) ** 3
y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)

heart_line, = ax.plot(x, y, color='pink', linewidth=3)

small_hearts = []

for i in range(12):
    small_heart, = ax.plot([], [], color='pink', linewidth=0.5)
    small_hearts.append(small_heart)

def update(i):
    
    for small_heart in small_hearts:
        small_heart.set_data([], [])

    text.set_text("RAWAN")

    angles = np.linspace(0, 2 * np.pi, len(small_hearts))
    radius = 20
    small_x = radius * np.sin(angles + i * 0.1)
    small_y = radius * np.cos(angles + i * 0.1)

    for small_heart, small_x_val, small_y_val in zip(small_hearts, small_x, small_y):
        small_heart.set_data(x + small_x_val, y + small_y_val)


animation = FuncAnimation(fig, update, frames=100, interval=50, repeat="true")


text = ax.text(0, -5, "", color='pink', fontsize=20, ha='center')


ax.set_xlim(-35, 35)
ax.set_ylim(-35, 35)
ax.axis('off')

plt.show()
