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
    (ball_x,ball_y,ball_vx,ball_vy,
    ball2_x,ball2_y,ball2_vx,ball2_vy)=z
    ball_dx_dt=ball_vx
    ball_dy_dt=ball_vy
    ball_dvx_dt=0
    ball_dvy_dt=-g
    ball2_dx_dt=ball2_vx
    ball2_dy_dt=ball2_vy
    ball2_dvx_dt=0
    ball2_dvy_dt=-g
    return (ball_dx_dt,ball_dy_dt,ball_dvx_dt,ball_dvy_dt,
            ball2_dx_dt,ball2_dy_dt,ball2_dvx_dt,ball2_dvy_dt)

def fragment_collision_check(ball_x0,ball_y0,ball_vx0,ball_vy0,ball2_x0,ball2_y0,ball2_vx0,ball2_vy0):
    distance=ball_y0-ground_y

    if distance<=ball_r:
        ball_vx=ball_vx0
        ball_vy=ball_y0*(ball_m+ground_m)/(ball_m+ground_m)+2*ground_m*ground_vy0/(ball_m+ground_m)
    else:
        ball_vx=ball_vx0
        ball_vy=ball_vy0

    distance=ball2_y0-ground_y

    if distance<=ball2_r:
        ball2_vx=ball2_vx0
        ball2_vy=ball2_y0*(ball2_m+ground_m)/(ball2_m+ground_m)+2*ground_m*ground_vy0/(ball2_m+ground_m)
    else:
        ball2_vx=ball2_vx0
        ball2_vy=ball2_vy0
    return ball_vx,ball_vy,ball2_vx,ball2_vy

def calc(ball_x0,ball_y0,ball_vx0,ball_vy0,ball2_x0,ball2_y0,ball2_vx0,ball2_vy0):
    coords_ball_x=[ball_x0]
    coords_ball_y=[ball_y0]
    
    coords_ball2_x=[ball2_x0]
    coords_ball2_y=[ball2_y0]

    for frame in range(frames-1):
        t_fragment=[t[frame],t[frame+1]]
        z0=(coords_ball_x[-1],coords_ball_y[-1],ball_vx0,ball_vy0,
            coords_ball2_x[-1],coords_ball2_y[-1],ball2_vx0,ball2_vy0)

        fragment_solution=odeint(fragment_movement_solve,z0,t_fragment)

        ball_x_last=fragment_solution[1,0]
        ball_y_last=fragment_solution[1,1]
        ball_vx_last=fragment_solution[1,2]
        ball_vy_last=fragment_solution[1,3]

        coords_ball_x.append(ball_x_last)
        coords_ball_y.append(ball_y_last)

        ball2_x_last=fragment_solution[1,4]
        ball2_y_last=fragment_solution[1,5]
        ball2_vx_last=fragment_solution[1,6]
        ball2_vy_last=fragment_solution[1,7]

        coords_ball2_x.append(ball2_x_last)
        coords_ball2_y.append(ball2_y_last)

        collision_check=fragment_collision_check(ball_x_last,ball_y_last,ball_vx_last,ball_vy_last,ball2_x_last,ball2_y_last,ball2_vx_last,ball2_vy_last)
        ball_vx0=collision_check[0]
        ball_vy0=collision_check[1]
        ball_vx0=collision_check[2]
        ball_vy0=collision_check[3]

    return coords_ball_x,coords_ball_y,coords_ball2_x,coords_ball2_y

def animate(i):
    ball_x=coords_ball_x[i]
    ball_y=coords_ball_y[i]
    ball2_x=coords_ball2_x[i]
    ball2_y=coords_ball2_y[i]
    ball.set_data([ball_x],[ball_y])
    ball2.set_data([ball2_x],[ball2_y])


if __name__=='__main__':
    #границы
    ground_w=300
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
    #окружность2
    ball2_r=20
    ball2_m=1
    ball2_x0=25
    ball2_y0=100
    ball2_vx0=0
    ball2_vy0=0
    ball2_e=1

    coords_ball_x,coords_ball_y,coords_ball2_x,coords_ball2_y=calc(ball_x0,ball_y0,ball_vx0,ball_vy0,ball2_x0,ball2_y0,ball2_vx0,ball2_vy0)
    
    fig,ax=plt.subplots()

    ball,=plt.plot([],[],'o',color='b',ms=ball_r*5)
    ball2,=plt.plot([],[],'o',color='r',ms=ball2_r*5)

    ground,=plt.plot([ground_x,ground_x+ground_w],[ground_y,ground_y],'-',color='r')

    a=FuncAnimation(fig,animate,frames=frames,interval=interval)

    edge=100
    plt.axis('equal')
    ax.set_xlim(0,edge)
    ax.set_ylim(0,edge)

    a.save('result.gif',writer='pillow')