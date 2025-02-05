import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x=np.arange(-5,5,0.1)

def diff_func(i,x):
    y,z=i
    dy_dx=y**2*z
    dz_dx=z/x-y*z**2
    return dy_dx,dz_dx

y0=1
z0=-3
i0=y0,z0

s=odeint(diff_func,i0,x)
plt.plot(x,s)

plt.savefig('task_1_1.png')