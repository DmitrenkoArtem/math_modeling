import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x=np.arange(0,0.1,0.001)

def diff_func(i,x):
    k,y=i
    
    dk_dx=(k**2-(3*y**2)/x**0.5)/y
    dy_dx=k
 
    return dk_dx,dy_dx

y0=0
k0=1
i0=k0,y0

s=odeint(diff_func,i0,x)
plt.plot(x,s)
plt.savefig('task_2_2.png')