#Assignment 2
# Problem 11
# U=[u1,u2,u3]
# U'=f(t,U)=[u1+2u2-2u3+exp(-t),u2+u3-2exp(-t),u1+2u2+exp(-t)]

import numpy as np
import matplotlib.pyplot as pt

U=np.array([3.0,-1.0,1.0])# initialising U vector 
u1=[3.0];u2=[-1.0];u3=[1.0] # u array
def f(t,U):
 return(np.array([U[0]+2.0*U[1]-2.0*U[2]+np.exp(-t),U[1]+U[2]-2.0*np.exp(-t),U[0]+2.0*U[1]+np.exp(-t)]))
h=0.1 #step size
T=np.linspace(0.0,1.0,int(1.0/h)+1)
#RK4 loop
for t in T[:T.size-1]:
 k1=h*f(t,U)
 k2=h*f(t+h/2.0,U+k1/2.0)
 k3=h*f(t+h/2.0,U+k2/2.0)
 k4=h*f(t+h,U+k3)
 U=U+(k1+2.0*k2+2.0*k3+k4)/6.0
 u1+=[U[0]];u2+=[U[1]];u3+=[U[2]]

pt.plot(T,u1,'g-',label='u1')
pt.plot(T,u2,'c-',label='u2')
pt.plot(T,u3,'m-',label='u3')
pt.xlabel("t")
pt.ylabel("u")
pt.legend()
pt.show()
