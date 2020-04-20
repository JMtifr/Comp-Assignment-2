#Assignment 2
# Problem 5
#y"=-10
# bc :: y(0)=0, y(10)=0
# p=y', y"=p'
# We solve this problem by shooting method and assume that we don't know behaviour of y(x) with initial y' 

import numpy as np
import matplotlib.pyplot as pt

def es(x): # exact solution
 return(-5*x*x+50*x)

def dp(x,y,p): # this function return y"
 return(-10.0)
h=0.1 #step size
g=10.0 # given 

x=np.linspace(0.0,10.0,10.0/h+1) # creating x array
def RK(ti) : # function will return solution of ivp with y'=t
 y=[0.0] # creating y array
 Y=0.0 #  y(0)=0
 P=ti
 # -------------RK4 loop---------------------------------
 for t in x[1:len(x)]: 
  k11=h*dp(t,Y,P)
  k12=h*P
  k21=h*dp(t+h/2.0,Y+k12/2.0,P+k11/2.0)
  k22=h*(P+k11/2.0)
  k31=h*dp(t+h/2.0,Y+k22/2.0,P+k21/2.0)
  k32=h*(P+k21/2.0)
  k41=h*dp(t+h,Y+k32,P+k31)
  k42=h*(P+k31)
  P=P+(k11+2.0*k21+2.0*k31+k41)/6.0 # evaluating P(i+1)
  Y=Y+(k12+2.0*k22+2.0*k32+k42)/6.0 # evaluating Y(i+1)
  y=y+[Y] # adding data to y array
 #--------------------------------------------------------
 d=Y # taking last Y value, i.e. y(10)
 return(d,y)

# ++++++++++++++++++++++++ Solving by bisection method+++++++++++++++++++++++++++++++++++++++++
# 1st we shall find 2 initial y' for which y(10) are in opposite sign
t=1.0 # initial guess of y'
d,y=RK(t)
tt=0
d1=d;d2=d # initialising to enter in loop
pt.subplot(1,2,1)
while d1*d2>0.0:
 d2=d1
 tt=t # storing previous y'
 if d1>0.0:
  t=t-1.0
 else:
  t=t+1.0
 pt.plot(x,y,'y:',label='candidate solutions')
 d1,y=RK(t)
# Now we have 2 y' for which y(10) are in opposite sign => t,tt
# finding optimal iv y' by bisection method
t1=t
t2=tt
d1,y=RK(t1);d2,y=RK(t2)
while abs(d)>0.001: 
  t=(t1+t2)/2.0
  d,y=RK(t)
  if d*d1>0:
   t1=t
  else:
   t2=t

d,y=RK(t)

pt.plot(x,es(x),'b-',label='Exact solution')
pt.plot(x,y,'r--',label='numerical solution')
pt.legend()
pt.title("Bisection method")
pt.xlabel("x");pt.ylabel("y")
pt.ylim(bottom=0)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#=========== Finding solutionby random guess of initial value=====================================
# In this method we asssume that we know a narrow range of initial value 
yr=[];dr=[] #Array for storing solutions  
pt.subplot(1,2,2)
for i in range(100):
 t=40.0+20.0*np.random.random_sample() # generating random numbers among 40 to 60
 d,y=RK(t)
 pt.plot(x,y,'c:',label='candidate solutions')
 dr=dr+[abs(d)] #storing |y(10)| values
 yr=yr+[y] 
y=yr[np.argmin(dr)] # taking solution which has minimum y(10) value
pt.plot(x,es(x),'m-',label='Exact solution')
pt.plot(x,y,'k--',label='numerical solution')
pt.legend()
pt.title("Random guess of initial value")
pt.xlabel("x");pt.ylabel("y")
pt.ylim(bottom=0) 
pt.show()
