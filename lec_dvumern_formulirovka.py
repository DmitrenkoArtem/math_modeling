import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames=100
seconds_in_year=365*24*60*60
years=1
t=np.linspace(0,years*seconds_in_year,frames)

	
def move_func(z,t):
    x,y,vx,vy=z
    dx_dt=vx
    dy_dt=vy
    dvx_dt=-G*M*x/(x**2+y**2)**1.5
    dvy_dt=-G*M*y/(x**2+y**2)**1.5
    return dx_dt,dy_dt,dvx_dt,dvy_dt

	
G=6.67*10**(-11)
M=1.998*10**(30)
 
x0=149*10**9
y0=0
vx0=0
vy0=30000

z0=x0,y0,vx0,vy0

s=odeint(move_func,z0,t)

fig,ax=plt.subplots()
ball,=plt.plot([],[],'o',color='r')
ball_line,=plt.plot([],[],'-',color='r')

def animate(i):
    ball.set_data([s[i][0]],[s[i][1]])
    ball_line.set_data(s[:i,0],s[:i,1])
	
a=FuncAnimation(fig,animate,frames=frames,interval=20)
	
 
plt.plot([0],[0],'o',color='y',ms=20)

edge=2*x0
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
 
a.save('lec_dvumern_formulirovka.gif',writer='pillow')