import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

time = 15  # продолжительность (с)
interval = 20  # время между кадрами (мс)
frames = int(time * 1000 / interval)  # количество кадров (исправлено)

g = 9.8

t = np.linspace(0, time, frames)  # время разделено на отрезки

def fragment_movement_solve_func(z, t):
    (rect_x, rect_y, rect_vx, rect_vy, rect_a, rect_omega) = z
    dx_dt = rect_vx
    dy_dt = rect_vy
    dvx_dt = 0
    dvy_dt = -g
    da_dt = rect_omega
    domega_dt = 0
    return dx_dt, dy_dt, dvx_dt, dvy_dt, da_dt, domega_dt

def fragment_collision_check_func(rect_vx, rect_vy, rect_omega, rect_datax, rect_datay, rect_rotaxis_x, rect_rotaxis_y, rect_x, rect_y):
    rect_y_min = min(rect_datay)  # минимальная координата прямоугольника по y
    rect2_y_max = max(rect2_datay0)  # максимальная координата прямоугольника 2 по y
    distance_x = min(rect2_datax0) - max(rect_datax)
    distance_y = rect_y_min - rect2_y_max
    ground_distance = rect_y_min - ground_y

    if distance_y <= 0:
        if ground_distance > 0:
            if distance_x <= 0:  # если прямоугольники пересекаются по х, то они сталкиваются
                rect_vy = -rect_vy * rect_k  # Абсолютно упругий удар
                if distance_x < rect_w:  # если прямоугольник выходит за границы, то он отталкивается в сторону
                    rect_rotaxis_x, rect_rotaxis_y = get_collision_rotaxis_func(rect_datax, rect_datay, rect_x, rect_y)
                    rect_vx = -10
                    rect_omega = np.pi / 3.5  # Установка угловой скорости
        else:
            # Столкновение с землей
            rect_rotaxis_x, rect_rotaxis_y = get_collision_rotaxis_func(rect_datax, rect_datay, rect_x, rect_y)
            rect_vy = -rect_vy * rect_k  # Абсолютно упругий удар
            rect_omega = np.pi / 3.5  # Установка угловой скорости при ударе о землю
    return rect_vx, rect_vy, rect_omega, rect_rotaxis_x, rect_rotaxis_y

def get_collision_rotaxis_func(rect_datax, rect_datay, rect_x, rect_y):
    # Находим самую нижнюю точку прямоугольника (которая и станет точкой вращения)
    collision_point_index = np.argmin(rect_datay)
    collision_rotaxis_x = rect_datax[collision_point_index] - rect_x
    collision_rotaxis_y = rect_datay[collision_point_index] - rect_y
    return collision_rotaxis_x, collision_rotaxis_y

def seq_calc_func(rect_x, rect_y, rect_vx, rect_vy, rect_a, rect_omega, rect_rotaxis_x, rect_rotaxis_y):
    seq_rect_datax = [rect_datax0]  # последовательность данных по x
    seq_rect_datay = [rect_datay0]  # последовательность данных по y

    for frame in range(frames - 1):
        fragment_t = [t[frame], t[frame + 1]]  # временной отрезок
        fragment_z0 = (rect_x, rect_y, rect_vx, rect_vy, rect_a, rect_omega)

        fragment_solution = odeint(fragment_movement_solve_func, fragment_z0, fragment_t)

        rect_x = fragment_solution[1, 0]
        rect_y = fragment_solution[1, 1]
        rect_vx = fragment_solution[1, 2]
        rect_vy = fragment_solution[1, 3]
        rect_a = fragment_solution[1, 4]
        rect_omega = fragment_solution[1, 5]

        # Вычисление новых координат с учетом вращения
        fragment_rect_datax = (rect_fig_x - rect_rotaxis_x) * np.cos(rect_a) - (rect_fig_y - rect_rotaxis_y) * np.sin(rect_a) + rect_rotaxis_x + rect_x
        fragment_rect_datay = (rect_fig_y - rect_rotaxis_y) * np.cos(rect_a) + (rect_fig_x - rect_rotaxis_x) * np.sin(rect_a) + rect_rotaxis_y + rect_y

        seq_rect_datax.append(fragment_rect_datax)
        seq_rect_datay.append(fragment_rect_datay)

        # Проверка столкновений и обновление параметров
        rect_vx, rect_vy, rect_omega, rect_rotaxis_x, rect_rotaxis_y = fragment_collision_check_func(
            rect_vx, rect_vy, rect_omega, fragment_rect_datax, fragment_rect_datay, rect_rotaxis_x, rect_rotaxis_y, rect_x, rect_y)

    return seq_rect_datax, seq_rect_datay

def animate_func(i):
    x = seq_rect_datax[i]
    y = seq_rect_datay[i]
    rect.set_data(x, y)
    return rect,

if __name__ == '__main__':
    # Параметры
    ground_w = 200
    ground_m = 1e30
    ground_x = -100
    ground_y = 5

    rect_w = 20
    rect_h = 10
    rect_m = 100
    rect_x0 = 40
    rect_y0 = 60
    rect_vx0 = 0
    rect_vy0 = 0
    rect_a0 = 0
    rect_omega0 = 0
    rect_rotaxis_x0 = 0
    rect_rotaxis_y0 = 0
    rect_k = 0.6

    rect2_w = 60
    rect2_h = 20
    rect2_m = 1e30
    rect2_x0 = 70
    rect2_y0 = ground_y

    # Инициализация фигур
    fig, ax = plt.subplots()
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)

    rect_fig_x = np.array([-rect_w/2, rect_w/2, rect_w/2, -rect_w/2, -rect_w/2])
    rect_fig_y = np.array([-rect_h/2, -rect_h/2, rect_h/2, rect_h/2, -rect_h/2])
    rect_datax0 = rect_fig_x + rect_x0
    rect_datay0 = rect_fig_y + rect_y0
    rect, = plt.plot([], [], '-', color='b')

    rect2_fig_x = np.array([0, rect2_w/2, rect2_w/2, -rect2_w/2, -rect2_w/2, 0])
    rect2_fig_y = np.array([0, 0, rect2_h, rect2_h, 0, 0])
    rect2_datax0 = rect2_fig_x + rect2_x0
    rect2_datay0 = rect2_fig_y + rect2_y0
    rect2, = plt.plot(rect2_datax0, rect2_datay0, '-', color='r')

    ground, = plt.plot([ground_x, ground_x + ground_w], [ground_y, ground_y], '-', color='r')

    # Расчет анимации
    seq_rect_datax, seq_rect_datay = seq_calc_func(rect_x0, rect_y0, rect_vx0, rect_vy0, rect_a0, rect_omega0, rect_rotaxis_x0, rect_rotaxis_y0)

    # Создание анимации
    ani = FuncAnimation(fig, animate_func, frames=frames, interval=interval, blit=True)
    plt.show()
    ani.save('resulttt.gif', writer='pillow')