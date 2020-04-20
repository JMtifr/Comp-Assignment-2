#Assignment 2
# Problem no 2
# dy/dt=y/t-(y/t)^2
import numpy as np
import matplotlib.pyplot as pt

def f(x,y): # dy/dx
 return(y/x-(y/x)**2)
def ac(x): # actual solution
 return(x/(1.0+np.log(x)))

t=np.arange(1.0,2.1,0.1) # creating x axis
h=0.1 # given
y=[1.0];ya=[1.0] # initial value of y
ae=[0.0];re=[0.0] # array for errors

xy=1.0;aa=0.0;AE=0.0;RE=0.0

for i in t[1:len(t)]: # loop for solutions by Eular method
 xy=xy+h*f(i,xy) # calculating y(i+1) using Eular method
 y=y+[xy]
 aa=ac(i) # actual solution
 ya=ya+[aa]
 AE=abs(aa-xy) # absolute error
 RE=AE/aa # relative error
 ae=ae+[AE]
 re=re+[RE]

pt.subplot(2,1,1)
pt.plot(t,y,'r.-',label='Numerical solution')
pt.plot(t,ya,'b--',label='Exact solution')
pt.xlabel('t');pt.ylabel('y')
pt.title("Solution using Eular method")
pt.legend()
pt.subplot(2,1,2)
pt.plot(t,ae,'g.-',label='Absolute error')
pt.plot(t,re,'y.-',label='Relative error')
pt.xlabel('t');pt.ylabel('Error')
pt.title("Error to the solution")
pt.grid()
pt.legend()
pt.tight_layout()
pt.show() 
