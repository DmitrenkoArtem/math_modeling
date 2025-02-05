import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames=200
t=np.linspace(0,5,frames)

def move_func(z,t):
    x,y,vx,vy=z
    dxdt=vx
    dydt=vy
    dvxdt=0
    dvydt=-g
    return dxdt,dydt,dvxdt,dvydt

g=9.8
v=15
alpha=np.deg2rad(80)

x0=0
y0=0
vx0=v*np.cos(alpha)
vy0=v*np.sin(alpha)

z0=x0,y0,vx0,vy0

s=odeint(move_func,z0,t)

fig,ax=plt.subplots()
ball,=plt.plot([],[],'o',color='r')
ball_line,=plt.plot([],[],'-',color='r')

def animate(t):
    ball.set_data([s[t][0]],[s[t][2]])
    ball_line.set_data(s[:t,0],s[:t,2])
    return ball,ball_line,

a=FuncAnimation(fig,animate,frames=frames,interval=30)
edge=15
	
ax.set_xlim(0,edge)
ax.set_ylim(0,edge)
	
a.save('lec_second_law.gif', writer="pillow")