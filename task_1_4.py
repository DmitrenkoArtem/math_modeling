import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t=np.arange(-5,5,0.01)

def diff_func(i,t):
    k,y=i
    
    dk_dt=-5*y-k
    dy_dt=k
 
    return dk_dt,dy_dt

y0=4
k0=-1
i0=k0,y0

s=odeint(diff_func,i0,t)
plt.plot(t,s)
plt.savefig('task_1_4.png')