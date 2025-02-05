import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

	
s0=1600 # Начальная площадь
e=1367 # Вт / м^2
k=340*10**(-8) # Подбираемый коэффициент

t=np.arange(0,10,0.1)

def func(s,t):
    dsdt=k*e*(s/np.pi)**0.5*s0*np.cos(np.pi/12*(t-12))
    return dsdt


v_t=odeint(func,s0,t)
plt.plot(t,v_t)

plt.xlabel('Время')
plt.ylabel('Площадь')

plt.savefig('task_2_2.png')