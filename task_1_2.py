import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t=np.arange(-1,1,0.01)

def diff_func(i,t):
    x,y=i
    dx_dt=3*x-2*y+(np.exp(1)**(3*t))/(np.exp(1)**t+1)
    dy_dt=x-((np.exp(1)**(3*t))/((np.exp(1)**t+1)))
    return dx_dt,dy_dt

x0=5
y0=-7
i0=x0,y0

s=odeint(diff_func,i0,t)
plt.plot(t,s)
plt.savefig('task_1_2.png')