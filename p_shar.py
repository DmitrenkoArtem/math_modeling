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
    (ball_x,ball_y,ball_vx,ball_vy)=z
    dx_dt=ball_vx
    dy_dt=ball_vy
    dvx_dt=0
    dvy_dt=-g
    return dx_dt,dy_dt,dvx_dt,dvy_dt

def fragment_collision_check(ball_x0,ball_y0,ball_vx0,ball_vy0):
    distance=ball_y0-ground_y

    if distance<=ball_r:
        ball_vx=ball_vx0
        ball_vy=ball_y0*(ball_m+ground_m)/(ball_m+ground_m)+2*ground_m*ground_vy0/(ball_m+ground_m)
    else:
        ball_vx=ball_vx0
        ball_vy=ball_vy0
    return ball_vx,ball_vy

def calc(ball_x0,ball_y0,ball_vx0,ball_vy0):
    coords_ball_x=[ball_x0]
    coords_ball_y=[ball_y0]
    
    for frame in range(frames-1):
        t_fragment=[t[frame],t[frame+1]]
        z0=(coords_ball_x[-1],coords_ball_y[-1],ball_vx0,ball_vy0)

        fragment_solution=odeint(fragment_movement_solve,z0,t_fragment)

        ball_x_last=fragment_solution[1,0]
        ball_y_last=fragment_solution[1,1]
        ball_vx_last=fragment_solution[1,2]
        ball_vy_last=fragment_solution[1,3]

        coords_ball_x.append(ball_x_last)
        coords_ball_y.append(ball_y_last)
        collision_check=fragment_collision_check(ball_x_last,ball_y_last,ball_vx_last,ball_vy_last)
        ball_vx0=collision_check[0]
        ball_vy0=collision_check[1]

    return coords_ball_x,coords_ball_y

def animate(i):
    x=coords_ball_x[i]
    y=coords_ball_y[i]
    ball.set_data([x],[y])


if __name__=='__main__':
    #границы
    ground_w=200
    ground_m=0
    ground_x=-100
    ground_y=5
    ground_vx0=0
    ground_vy0=0
    #окружность
    ball_r=20
    ball_m=1
    ball_x0=25
    ball_y0=50
    ball_vx0=5
    ball_vy0=0
    ball_e=1

    coords_ball_x,coords_ball_y=calc(ball_x0,ball_y0,ball_vx0,ball_vy0)
    
    fig,ax=plt.subplots()
    ball,=plt.plot([],[],'o',color='b',ms=ball_r*5)
    ground,=plt.plot([ground_x,ground_x+ground_w],[ground_y,ground_y],'-',color='r')

    a=FuncAnimation(fig,animate,frames=frames,interval=interval)

    edge=100
    plt.axis('equal')
    ax.set_xlim(0,edge)
    ax.set_ylim(0,edge)

    a.save('result shar.gif',writer='pillow')