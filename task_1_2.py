import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t=np.arange(0,10,1)

def func(n,t):
    dndt=n*2
    return dndt

n0=1
n_t=odeint(func,n0,t)
plt.plot(t,n_t[:,:n0*10])

plt.xlabel('Время')
plt.ylabel('Количество')

plt.savefig('task_1_1.png')