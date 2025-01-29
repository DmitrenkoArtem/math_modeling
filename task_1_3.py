import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

v0=0
a=1
m=1
gamma=0.1
t=np.arange(0,10,0.1)

def func(v,t):
    dvdt=a-(v**2*gamma)/m
    return dvdt


v_t=odeint(func,v0,t)
plt.plot(t,v_t)

plt.xlabel('Время')
plt.ylabel('Скорость')

plt.savefig('task_1_3.png')