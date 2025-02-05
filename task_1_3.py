import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t=np.arange(-5,5,0.01)

def diff_func(i,t):
    k,y=i
    
    dk_dt=np.sin(t)+np.cos(t)
    dy_dt=k
 
    return dk_dt,dy_dt

y0=3
k0=0
i0=k0,y0

s=odeint(diff_func,i0,t)
plt.plot(t,s)
plt.savefig('task_1_3.png')