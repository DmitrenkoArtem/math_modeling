from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

alpha=1

def circle_move(vx0, vy0, time, angle_vel):
    x_square = np.array([0, 2, 2, 0, 0]) - 1
    y_square = np.array([0, 0, 2, 2, 0]) - 1

    # Поступательное движение
    x0 =3
    y0 =3
    a=-1
    b=-1
    x = x0 + x_square
    y = y0 + y_square

    alpha = angle_vel * time
    X = (x-x0-a) * np.cos(alpha) - (y-y0-b) * np.sin(alpha) + x0 + a
    Y = (y-y0-b) * np.cos(alpha) + (x-x0-a) * np.sin(alpha) + y0 + b
    return X, Y

    # if time > 50:
    #     alpha = - np.pi / 3
    #     X = (x-a) * np.cos(alpha) - (y-b) * np.sin(alpha) + x0 +a
    #     Y = (y-b) * np.cos(alpha) + (x-a) * np.sin(alpha) + y0+b
    #     return X, Y
    # else:
    #     return x, y


fig, ax = plt.subplots()
ball, = plt.plot([], [], '-', color='r', label='Ball')


def animate(i):
    ball.set_data(circle_move(vx0=0.01, vy0=0.01, time=i, angle_vel=i/1000))
    return ball,


edge = 10
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

ani = FuncAnimation(fig, animate, frames=100, interval=30)
ani.save('animation_3.gif', writer="pillow")