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
    ve_x,ve_y,ve_vx,ve_vy,
    pha_x,pha_y,pha_vx,pha_vy)=z
    
    ea_dx_dt=ea_vx
    ea_dy_dt=ea_vy
    ea_dvx_dt=-G*M*ea_x/(ea_x**2+ea_y**2)**1.5
    ea_dvy_dt=-G*M*ea_y/(ea_x**2+ea_y**2)**1.5
    
    me_dx_dt=me_vx
    me_dy_dt=me_vy
    me_dvx_dt=-G*M*me_x/(me_x**2+me_y**2)**1.5
    me_dvy_dt=-G*M*me_y/(me_x**2+me_y**2)**1.5
     
    ma_dx_dt=ma_vx
    ma_dy_dt=ma_vy
    ma_dvx_dt=-G*M*ma_x/(ma_x**2+ma_y**2)**1.5
    ma_dvy_dt=-G*M*ma_y/(ma_x**2+ma_y**2)**1.5
    
    ve_dx_dt=ve_vx
    ve_dy_dt=ve_vy
    ve_dvx_dt=-G*M*ve_x/(ve_x**2+ve_y**2)**1.5
    ve_dvy_dt=-G*M*ve_y/(ve_x**2+ve_y**2)**1.5

    pha_dx_dt=pha_vx
    pha_dy_dt=pha_vy
    pha_dvx_dt=-G*M*pha_x/(pha_x**2+pha_y**2)**1.5
    pha_dvy_dt=-G*M*pha_y/(pha_x**2+pha_y**2)**1.5
    
    return (ea_dx_dt,ea_dy_dt,ea_dvx_dt,ea_dvy_dt,
            me_dx_dt,me_dy_dt,me_dvx_dt,me_dvy_dt,
            ma_dx_dt,ma_dy_dt,ma_dvx_dt,ma_dvy_dt,
            ve_dx_dt,ve_dy_dt,ve_dvx_dt,ve_dvy_dt,
            pha_dx_dt,pha_dy_dt,pha_dvx_dt,pha_dvy_dt)

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

pha_x0=240*10**9
pha_y0=0
pha_vx0=0
pha_vy0=20122

z0=(ea_x0,ea_y0,ea_vx0,ea_vy0,
   me_x0,me_y0,me_vx0,me_vy0,
   ma_x0,ma_y0,ma_vx0,ma_vy0,
   ve_x0,ve_y0,ve_vx0,ve_vy0,
   pha_x0,pha_y0,pha_vx0,pha_vy0)

s=odeint(move_func,z0,t)
print(s)

fig,ax=plt.subplots()

earth,=plt.plot([],[],'o',color='b')
earth_line,=plt.plot([],[],'-',color='b')

mercury,=plt.plot([],[],'o',color='grey')
mercury_line,=plt.plot([],[],'-',color='grey')

mars,=plt.plot([],[],'o',color='r')
mars_line,=plt.plot([],[],'-',color='r')

venus,=plt.plot([],[],'o',color='k')
venus_line,=plt.plot([],[],'-',color='k')

phaethon,=plt.plot([],[],'o',color='brown')
phaethon_line,=plt.plot([],[],'-',color='brown')

def animate(i):
    earth.set_data([s[i][0]],[s[i][1]])
    earth_line.set_data(s[:i,0],s[:i,1])
    
    mercury.set_data([s[i][2]],[s[i][3]])
    mercury_line.set_data(s[:i,2],s[:i,3])
    
    mars.set_data([s[i][4]],[s[i][5]])
    mars_line.set_data(s[:i,4],s[:i,5])
    
    venus.set_data([s[i][6]],[s[i][7]])
    venus_line.set_data(s[:i,6],s[:i,7])

    phaethon.set_data([s[i][8]],[s[i][9]])
    phaethon_line.set_data(s[:i,8],s[:i,9])

a=FuncAnimation(fig,animate,frames=frames,interval=20)


#sun,=plt.plot([0],[0],'o',color='y',ms=20)

edge=4*ma_x0
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

a.save('lec_1_1.gif',writer='pillow')