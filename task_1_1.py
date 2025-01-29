import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

k=0.1
t=np.arange(0,30,1)

def func(n,t):
    dndt=n*k
    return dndt

n0=1
n_t=odeint(func,n0,t)
plt.plot(t,n_t)

plt.xlabel('Время')
plt.ylabel('Количество')
plt.savefig('task_1_1.png')