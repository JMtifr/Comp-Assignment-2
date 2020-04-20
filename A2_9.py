# Assignment 2
# Problem 9
# RK4
# 
import numpy as np
import matplotlib.pyplot as pt

def f(x,y): # y'
 return((y+y*y)/x)

def Rk4(h,x,y): # Rk4 one iteration
 k1=h*f(x,y)
 k2=h*f(x+h/2.0,y+k1/2.0)
 k3=h*f(x+h/2.0,y+k2/2.0)
 k4=h*f(x+h,y+k3)
 return(y+(k1+2.0*k2+2.0*k3+k4)/6.0)

x=1.0;y=-2.0 # initial values
acc=0.0001 # desiered accuracy
X=[1.0];Y=[-2.0] # arrays for x & y

while(x<=3.0):
 h=0.1 # initial step size
 ro=0.9 # initialising ro to enter in loop
 while(ro<1):
  Y1=Rk4(h,x,y)
  Y1=Rk4(h,x+h,Y1) # getting value of y(x+2h) with step size h
  Y2=Rk4(2.0*h,x,y) # getting value of y(x+2h) with step size 2h
  ro=30.0*h*acc/abs(Y1-Y2)
  if ro>1.0:
   hh=h*ro**0.25 # this is optimist step size
  else:
   h=h/10.0
 y=Rk4(hh,x,y)
 x=x+hh
 X+=[x]
 Y+=[y]
pt.plot(X,Y,'bs--')
pt.xlim(right=3)
pt.xlabel("x")
pt.ylabel("y")
pt.title("Solution with adaptive step size control")
pt.show()
