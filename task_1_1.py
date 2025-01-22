import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t=np.arange(0,100,0.01)

def func(n,t):
    dndt=n
    return dndt

n0=1
n_t=odeint(func,n0,t)
plt.plot(t,n_t)

plt.xlabel('Время')
plt.ylabel('Количество')

plt.savefig('task_1_1.png')