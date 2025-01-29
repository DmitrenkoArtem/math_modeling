import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

k=0.08
t=np.arange(0,4,0.1)

def func(n,t):
    dndt=-k*n
    return dndt

n0=1000
n_t=odeint(func,n0,t)
plt.plot(t,n_t)

plt.xlabel('Время')
plt.ylabel('Количество')

plt.savefig('task_1_2.png')