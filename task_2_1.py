import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t=np.arange(-1,1,0.01)

def diff_func(i,t):
    x,y,z=i
    dx_dt=3*x-y+z
    dy_dt=x+y+z
    dz_dt=4*x-y+4*z
 
    return dx_dt,dy_dt,dz_dt

x0=-71
y0=1
z0=-3
i0=x0,y0,z0

s=odeint(diff_func,i0,t)
plt.plot(t,s)
plt.savefig('task_2_1.png')