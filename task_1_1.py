import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames=100
seconds_in_year=365*24*60*60
years=1
t=np.linspace(0,years*seconds_in_year,frames)

def move_func(z,t):
    (ea_x,ea_y,ea_vx,ea_vy,
    me_x,me_y,me_vx,me_vy,
    ma_x,ma_y,ma_vx,ma_vy,
    ve_x,ve_y,ve_vx,ve_vy)=z
    ea_dx_dt=ea_vx
    ea_dy_dt=ea_vy
    ea_dvx_dt=-G*M*ea_x/(ea_x**2+ea_y**2)**1.5
    ea_dvy_dt=-G*M*ea_y/(ea_x**2+ea_y**2)**1.5
    return ea_dx_dt,ea_dy_dt,ea_dvx_dt,ea_dvy_dt

G=6.67*10**(-11)
M=1.998*10**(30)
 
ea_x0=149*10**9
ea_y0=0
ea_vx0=0
ea_vy0=30000

me_x0=58*10**9
me_y0=0
me_vx0=0
me_vy0=48000

ma_x0=228*10**9
ma_y0=0
ma_vx0=0
ma_vy0=24000

ve_x0=108*10**9
ve_y0=0
ve_vx0=0
ve_vy0=35000

z0=(ea_x0,ea_y0,ea_vx0,ea_vy0,
   me_x0,me_y0,me_vx0,me_vy0,
   ma_x0,ma_y0,ma_vx0,ma_vy0,
   ve_x0,ve_y0,ve_vx0,ve_vy0)

s=odeint(move_func,z0,t)

fig,ax=plt.subplots()
ball,=plt.plot([],[],'o',color='r')
ball_line,=plt.plot([],[],'-',color='r')

def animate(i):
    ball.set_data([s[i][0]],[s[i][1]])
    ball_line.set_data(s[:i,0],s[:i,1])
	
a=FuncAnimation(fig,animate,frames=frames,interval=20)
	
 
plt.plot([0],[0],'o',color='y',ms=20)

edge=2*ea_x0
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
 
a.save('lec_1_1.gif',writer='pillow')