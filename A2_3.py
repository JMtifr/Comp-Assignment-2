# Assignment 2
# Problem 3
# y"-2y'+y=xexp(x)-x 
# Let p=y' => p'-2p+y=xexp(x)-x
# r=[p,y]
# f=[p',p]
# k1=hf(r,x)
# k2=hf(r+k1/2,x+h/2)
# k3=hf(r+k2/2,x+h/2)
# k4=hf(r+k3,x+h)
# r(i+1)=r(i)+(k1+2k2+2k3+k4)/6
import numpy as np
import matplotlib.pyplot as pt

def dp(x,y,p): # y"=p'=(2p-y+xexp(x)-x)
 return(2*p-y+x*np.exp(x)-x)


h=0.05 # step size
x=np.linspace(0.0,1.0,1.0/h+1) # creating x array
y=[0] # y array
P=0.0;Y=0.0 # initial values
#---------- RK4 loop---------------------------------------------------
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
#-----------------------------------------------------------------------

pt.plot(x,y,'g.-')
pt.title("Solution by RK4 method")
pt.xlabel("x")
pt.ylabel("y")
pt.show() 
