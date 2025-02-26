import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames=200
t=np.linspace(0,5,frames)

def move_func(z,t):
    x,y,vx,vy=z
    
    dx_dt=vx
    dy_dt=vy
    dvx_dt=-k*vx**2
    dvy_dt=-g-k*vy**2
    
    return dx_dt,dy_dt,dvx_dt,dvy_dt

alpha=np.deg2rad(60)

m=0.5
k=0.1/m/1
g=9.8

v0=20
x0=0
y0=0

vx0=np.cos(alpha)*v0
vy0=np.sin(alpha)*v0

z0=x0,y0,vx0,vy0

s=odeint(move_func,z0,t)

fig,ax=plt.subplots()
ball,=plt.plot([],[],'o',color='r')
ball_line,=plt.plot([],[],'-',color='r')

def animate(t):
    ball.set_data([s[t][0]],[s[t][2]])
    ball_line.set_data(s[:t,0],s[:t,2])

a=FuncAnimation(fig,animate,frames=frames,interval=30)
edge=40
	
ax.set_xlim(0,edge)
ax.set_ylim(0,edge)
	
a.save('task_1_1_2.gif',writer="pillow")