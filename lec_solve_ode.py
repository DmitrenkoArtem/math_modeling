import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#Пределы изменения переменной величины
t=np.arange(0,10**6,100)
#дифференциальное уравнение в виде функции
def radio_function(m,t):
    dmdt=-k*m
    return dmdt
#Начальные условия
m_0=10
k=1.61*10**(-6) #постоянная распада для Висмута 210
m_t=odeint(radio_function,m_0,t)
plt.plot(t,m_t[:,0])
plt.savefig('lec_solve_ode.png')