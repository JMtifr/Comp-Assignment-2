#Assignment 2
# Problem 1
# (1) dy/dx=-9y
# (2) dy/dx=-20*(y-x)^2+2x
# Eular backward method
# y(i+1)=y(i)+hf(x(i+1),y(i+1))
# 1st equation => y(i+1)=y(i)/(1+9h)
# 2nd equation => y(i+1)=(40x(i+1)h-1+sqrt((1-40x(i+1)h)^2+80h(y(i)-20hx^2(i+1)+2hx(i+1)))/40h
import numpy as np
import matplotlib.pyplot as pt
def f1(y,h): # y(i+1) for eqn 1
 return(y/(1.0+9.0*h))
def f21(x,y,h): # y(i+1) for eqn 2 
 return(x+(-1.0+np.sqrt((1-40.0*h*x)**2+80.0*h*(y-20.0*h*x*x+2.0*h*x)))/40.0/h)
h=0.05
x=np.arange(0.0,1.0,h) # creating array for x
y1=[np.exp(1)] # initialising y eqn(1)
y21=[1/3.0] # initialising y eqn(2)

Y1=np.exp(1);Y2=1/3.0 
for i in x[1:len(x)]: # solving and filling arrays of y
 Y1=f1(Y1,h)
 y1=y1+[Y1]
 Y2=f21(i,Y2,h)
 y21=y21+[Y2]

pt.subplot(1,2,1)
pt.plot(x,y1,'go--')
pt.xlabel('X');pt.ylabel('Y')
pt.title('Solution of equation 1')
pt.subplot(1,2,2)
pt.plot(x,y21,'r^--')
pt.xlabel('X');pt.ylabel('Y')
pt.title('Solution of equation 2')
pt.tight_layout()
pt.show() 
