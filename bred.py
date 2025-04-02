import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Задаем сторону квадрата
a = 2  # длина стороны квадрата

# Определяем координаты вершин квадрата
square = np.array([[-a/2, -a/2],
                   [a/2, -a/2],
                   [a/2, a/2],
                   [-a/2, a/2],
                   [-a/2, -a/2]])  # Замыкаем квадрат

# Функция для вращения точки
def rotate(points, angle):
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                 [np.sin(angle), np.cos(angle)]])
    return points @ rotation_matrix.T

# Создаем фигуру и оси
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_aspect('equal')

# Инициализируем линию квадрата
line, = ax.plot([], [], lw=2)

# Функция инициализации анимации
def init():
    line.set_data([], [])
    return line,

# Функция обновления для анимации
def update(frame):
    angle = np.radians(frame)  # Преобразуем градусы в радианы
    rotated_square = rotate(square, angle)
    line.set_data(rotated_square[:, 0], rotated_square[:, 1])
    return line,

# Создаем анимацию
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 360, 2),
                              init_func=init, blit=True, interval=50)

# Показываем анимацию
ani.save('bred.gif',writer='pillow')