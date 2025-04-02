import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

time=6 #продолжительность (с)
interval=20 #время между кадрами (мс)
frames=int(1000/interval*time) #количество кадров

g=9.8
collisions=0

t=np.linspace(0,time,frames) #время разделено на отрезки

def fragment_movement_solve_func(z,t):
    (rect_x,rect_y,rect_vx,rect_vy,rect_a,rect_omega)=z
    dx_dt=rect_vx
    dy_dt=rect_vy
    dvx_dt=0
    dvy_dt=-g
    da_dt=rect_omega
    domega_dt=0
    return dx_dt,dy_dt,dvx_dt,dvy_dt,da_dt,domega_dt

def fragment_collision_check_func(rect_vx,rect_vy,rect_omega,rect_datax,rect_datay,rect_rotaxis_x,rect_rotaxis_y,rect_x,rect_y):
    rect_y_min=min(rect_datay) #минимальная координата прямоугольника по y
    rect2_y_max=max(rect2_datay0) #минимальная координата прямоугольнка 2 по y
    distance_x=min(rect2_datax0)-max(rect_datax)
    distance_to_rect_y=rect_y_min-rect2_y_max
    ground_distance=rect_y_min-ground_y
    if distance_to_rect_y<=0:
        if ground_distance>0:
            if distance_x<=0: #если прямоугольники пересекаются по х, то они сталкиваются
                rect_vy=-rect_vy*rect_k #Абсолютно упругий удар (rect_y*(rect_m+rect2_m)/(rect_m+rect2_m)+2*rect2_m*rect2_vy0/(rect_m+rect2_m))*rect_k
                if distance_x<rect_w: #если прямоугольник выходит за границы, то он отталкивается в сторону
                    rect_rotaxis_x,rect_rotaxis_y=get_collision_rotaxis_func(rect_datax,rect_datay,rect_x,rect_y)
                    rect_rotaxis_x=0 #начальный поворот прямоугольника=0, поэтому все координаты y будут минимальными. центр прямоугольника и граница прямоугольника 2 находится на одной координате х=0
                    rect_vx=-5
                    rect_omega=np.pi/4.5
                    print('столкновение с прямоугольником')
        else:
            rect_rotaxis_x,rect_rotaxis_y=get_collision_rotaxis_func(rect_datax,rect_datay,rect_x,rect_y)
            rect_vy=-rect_vy*rect_k #Абсолютно упругий удар (rect_y*(rect_m+ground_m)/(rect_m+ground_m)+2*ground_m*ground_vy0/(rect_m+ground_m))*rect_k
            print('столкновение с землей')
            
    return rect_vx,rect_vy,rect_omega,rect_rotaxis_x,rect_rotaxis_y

def get_collision_rotaxis_func(rect_datax,rect_datay,rect_x,rect_y):
    collision_point_index=np.argmin(rect_datay) #np.argmin возвращает индекс нижней координаты y
    collision_rotaxis_x=rect_datax[collision_point_index]-rect_x
    collision_rotaxis_y=rect_datay[collision_point_index]-rect_y
    global collisions
    collisions+=1
    print('УДАР',collisions,rect_datax[collision_point_index],rect_datay[collision_point_index])
    return collision_rotaxis_x,collision_rotaxis_y

def seq_calc_func(rect_x,rect_y,rect_vx,rect_vy,rect_a,rect_omega,rect_rotaxis_x,rect_rotaxis_y):
    seq_rect_datax=[rect_datax0] #последовательность данных по x
    seq_rect_datay=[rect_datay0] #последовательность данных по y
    
    for frame in range(frames-1):
        fragment_t=[t[frame],t[frame+1]] #выбор временного отрезка
        fragment_z0=(rect_x,rect_y,rect_vx,rect_vy,rect_a,rect_omega)

        fragment_solution=odeint(fragment_movement_solve_func,fragment_z0,fragment_t)

        rect_x=fragment_solution[1,0]
        rect_y=fragment_solution[1,1]
        rect_vx=fragment_solution[1,2]
        rect_vy=fragment_solution[1,3]
        rect_a=fragment_solution[1,4]
        rect_omega=fragment_solution[1,5]

        fragment_rect_datax=(rect_fig_x-rect_rotaxis_x)*np.cos(rect_a)-(rect_fig_y-rect_rotaxis_y)*np.sin(rect_a)+rect_x+rect_rotaxis_x
        fragment_rect_datay=(rect_fig_y-rect_rotaxis_y)*np.cos(rect_a)+(rect_fig_x-rect_rotaxis_x)*np.sin(rect_a)+rect_y+rect_rotaxis_y
        #fragment_rect_datax=(loxx-rect_rotaxis_x)*np.cos(rect_a)-(loxy-rect_rotaxis_y)*np.sin(rect_a)+rect_rotaxis_x+rect_x
        #fragment_rect_datay=(loxy-rect_rotaxis_y)*np.cos(rect_a)+(loxx-rect_rotaxis_x)*np.sin(rect_a)+rect_rotaxis_y+rect_y

        seq_rect_datax.append(fragment_rect_datax)
        seq_rect_datay.append(fragment_rect_datay)

        rect_vx,rect_vy,rect_omega,rect_rotaxis_x,rect_rotaxis_y=fragment_collision_check_func(rect_vx,rect_vy,rect_omega,fragment_rect_datax,fragment_rect_datay,rect_rotaxis_x,rect_rotaxis_y,rect_x,rect_y)

    return seq_rect_datax,seq_rect_datay

def animate_func(i):
    x=seq_rect_datax[i]
    y=seq_rect_datay[i]
    rect.set_data([x],[y])


if __name__=='__main__':
    #границы
    ground_w=200
    ground_m=1e30
    ground_x=-100
    ground_y=5

    ground_vy0=0

    #прямоугольники
    rect_w=20
    rect_h=10
    rect_m=5
    rect_x0=40
    rect_y0=60
    rect_vx0=0
    rect_vy0=0
    rect_a0=0
    rect_omega0=0
    rect_rotaxis_x0=0
    rect_rotaxis_y0=0
    rect_k=0.6 #коэффициент упругости

    rect2_w=60
    rect2_h=20
    rect2_m=1e30
    rect2_x0=70
    rect2_y0=ground_y
    rect2_vx0=0
    rect2_vy0=0
    rect2_a0=0


    fig,ax=plt.subplots()

    #координаты фигур, их начальное положение и создание
    rect_fig_x=np.array([-rect_w/2,rect_w/2,rect_w/2,-rect_w/2,-rect_w/2]) #x координаты прямоугольника
    rect_fig_y=np.array([-rect_h/2,-rect_h/2,rect_h/2,rect_h/2,-rect_h/2]) #y координаты прямоугольника
    rect_datax0=rect_fig_x+rect_x0 #начальные х данные графика
    rect_datay0=rect_fig_y+rect_y0 #начальные y данные графика
    rect,=plt.plot([],[],'-',color='b') #добавление графика

    rect2_fig_x=np.array([0,rect2_w/2,rect2_w/2,-rect2_w/2,-rect2_w/2,0]) #x координаты прямоугольника 2
    rect2_fig_y=np.array([0,0,rect2_h,rect2_h,0,0]) #y координаты прямоугольника 2
    rect2_datax0=rect2_fig_x+rect2_x0 #начальные х данные графика
    rect2_datay0=rect2_fig_y+rect2_y0 #начальные y данные графика
    rect2,=plt.plot(rect2_datax0,rect2_datay0,'-',color='r') #добавление графика
    
    ground,=plt.plot([ground_x,ground_x+ground_w],[ground_y,ground_y],'-',color='r') #добавление графика


    #получение данных для анимирования
    seq_rect_datax,seq_rect_datay=seq_calc_func(rect_x0,rect_y0,rect_vx0,rect_vy0,rect_a0,rect_omega0,rect_rotaxis_x0,rect_rotaxis_y0)
 

    a=FuncAnimation(fig,animate_func,frames=frames,interval=interval)


    edge=100
    plt.axis('equal')
    ax.set_xlim(-edge,edge)
    ax.set_ylim(0,edge)


    a.save('result.gif',writer='pillow')