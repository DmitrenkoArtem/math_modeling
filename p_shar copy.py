import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

time=10
interval=20
frames=time*interval

g=9.8

t=np.linspace(0,time,frames)

def fragment_movement_solve(z,t):
    (rect_x,rect_y,rect_vx,rect_vy)=z
    dx_dt=rect_vx
    dy_dt=rect_vy
    dvx_dt=0
    dvy_dt=-g
    return dx_dt,dy_dt,dvx_dt,dvy_dt

def fragment_collision_check(rect_x0,rect_y0,rect_vx0,rect_vy0):
    distance=rect_y0-ground_y

    if distance<=0:
        rect_vx=rect_vx0
        rect_vy=rect_y0*(rect_m+ground_m)/(rect_m+ground_m)+2*ground_m*ground_vy0/(rect_m+ground_m)
    else:
        rect_vx=rect_vx0
        rect_vy=rect_vy0
    return rect_vx,rect_vy

def calc(rect_x0,rect_y0,rect_vx0,rect_vy0):
    coords_rect_x=[rect_x0]
    coords_rect_y=[rect_y0]
    
    for frame in range(frames-1):
        t_fragment=[t[frame],t[frame+1]]
        z0=(coords_rect_x[-1],coords_rect_y[-1],rect_vx0,rect_vy0)

        fragment_solution=odeint(fragment_movement_solve,z0,t_fragment)

        rect_x_last=fragment_solution[1,0]
        rect_y_last=fragment_solution[1,1]
        rect_vx_last=fragment_solution[1,2]
        rect_vy_last=fragment_solution[1,3]




        rect_points_x_last=rect_points_x*np.cos(rect_a)-rect_points_y*np.sin(rect_a)
        rect_points_y_last=rect_points_y*np.sin(rect_a)-rect_points_x*np.cos(rect_a)



        coords_rect_x.append(rect_points_x_last)
        coords_rect_y.append(rect_points_y_last)




        collision_check=fragment_collision_check(rect_x_last,rect_y_last,rect_vx_last,rect_vy_last)
        rect_vx0=collision_check[0]
        rect_vy0=collision_check[1]

    return coords_rect_x,coords_rect_y

def animate(i):
    x=coords_rect_x[i]
    y=coords_rect_y[i]
    rect.set_data([x,y])


if __name__=='__main__':
    #границы
    ground_w=200
    ground_m=0
    ground_x=-100
    ground_y=5
    ground_vx0=0
    ground_vy0=0
    #окружность
    rect_w=20
    rect_h=10
    rect_m=1
    rect_x0=25
    rect_y0=50
    rect_vx0=5
    rect_vy0=0
    rect_e=1
    rect_a=1



    rect_points_x=np.array([0,rect_w,rect_w,0,0])
    rect_points_y=np.array([0,0,rect_h,rect_h,0])


    

    coords_rect_x,coords_rect_y=calc(rect_x0,rect_y0,rect_vx0,rect_vy0)
    
    fig,ax=plt.subplots()
    rect,=plt.plot([],[],'-',color='b',ms=5)
    ground,=plt.plot([ground_x,ground_x+ground_w],[ground_y,ground_y],'-',color='r')

    a=FuncAnimation(fig,animate,frames=frames,interval=interval)

    edge=100
    plt.axis('equal')
    ax.set_xlim(0,edge)
    ax.set_ylim(0,edge)

    a.save('result.gif',writer='pillow')