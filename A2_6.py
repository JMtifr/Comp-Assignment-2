# Assignment 2
# Problem 6
# y"=-g
# p=y', p'=y"=f(x,y,y')
# bv :: y(0)=0=y(10)
# (w(i+1)-2w(i)+w(i-1))/h^2=f(x(i),w(i),(w(i+1)-w(i-1))/2h)

import numpy as np
import matplotlib.pyplot as pt
h=0.1 # step size
N=int(10.0/h+1.0) # number of points
g=10.0 # given
a=0.0;b=0.0 # 1st & 2nd boundary values
def f(x,y,p): # function y"
 return(-g)
def Es(x): # Exact solution
 return(-5.0*x*x+50.0*x)

x=np.linspace(0.0,10.0,N) # creating x array
y=np.zeros(N);w=np.zeros(N) # creating y array 

def Rx(x,yy): # this function y array after one iteration of relaxation method
 w=np.zeros(N)
 y=[]
 for i in yy:
  y+=[i]
 w[0]=a;w[N-1]=b # bv
 y[0]=a;y[N-1]=b
 for i in range(1,N-1): # Gauss Seidel method
  w[i]=(y[i+1]+y[i-1]-h*h*f(x[i],y[i],(y[i+1]-y[i-1])/2.0/h))/2.0
  y[i]=w[i]
 return(w)

#---------------------------Relaxation method iterations ---------------------------------------
y[0]=a;y[N-1]=b # putting bv
for i in range(1,N-1):
 y[i]=0.0 # initial guess solution
d=1# initialising d to enter in loop
n=300 
while(d==1):
 for i in range(n): # running n iterations taking previous y array as initial solution
  w=Rx(x,y)
  y=w
 y1=w
 for i in range(n): # running next n iteration from y1 array
  w=Rx(x,y)
  y=w
 y2=w
 pt.plot(x,w,'y:',label="candidate solution")
 for j in range(1,N-1):
  if abs(y1[j]-y2[j])>0.001: # accuracy checking
   d=1
   break
  else:
   d=0
 y=y2 # storing y2 to y
#----------------------------------------------------------------------------------------------

pt.plot(x,Es(x),'b-',label="Exact soution")
pt.plot(x,y,'r--',label="Numerical solution")
pt.xlabel("x");pt.ylabel("y")
pt.title("Solution by Relaxation method")
pt.legend()
pt.show()
