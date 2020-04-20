# Assignment 2
# problem 13
# Eular method
# y'=p
# y"=p'
# xy"-2xy'+2y=x^3 lnx

import numpy as np
import matplotlib.pyplot as pt
 
# Y=[y,p], Y'=[p,p"]
def f(x,y):
 return(np.array([y[1],x**2*np.log(x)-2.0*y[0]/x+2.0*y[1]])) 
def exact(x): # exact solution
 return(7.0*x/4.0+x**3*np.log(x)/2.0-3.0/4.0*x**3)

h=0.001
Y=[1.0,0.0] # initial value
X=np.linspace(1.0,2.0,int(1.0/h)+1) # creating x array
y=[1.0] # y array
for x in X:
 Y=Y+h*f(x,Y) #Eular method
 y+=[Y[0]]

pt.plot(X,y[:len(X)],'c:',label="Numeric solution")
pt.plot(X,exact(X),'m-',label="Exact solution")
pt.legend()
pt.xlabel("x")
pt.ylabel("y")
pt.title("Eular method")
pt.show()
