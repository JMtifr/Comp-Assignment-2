# Assignment 2
# Problem 7
from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as pt

# y'
def f1(t,y):
  return(t*np.exp(3.0*t)-2.0*y)
def f2(t,y):
 return(1.0-(t-y)**2)
def f3(t,y):
 return(1.0+y/t)
def f4(t,y):
 return(np.cos(2.0*t)+np.sin(3.0*t))

# exact solutions by WolframAlpha
def e1(x):
 return((np.exp(-2*x)*(np.exp(5.0*x)*(5.0*x-1.0)+1.0))/25.0)
def e2(x):
 return(1.0/(x-3.0)+x)
def e3(x):
 return(x*(np.log(x)+2.0))
def e4(x):
 return(np.sin(2.0*x)/2.0-np.cos(3.0*x)/3.0+4.0/3.0)

# creating x array
t1=np.linspace(0,1,11)
t2=np.linspace(2.0,3.0,11)
t3=np.linspace(1.0,2.0,11)
t4=np.linspace(0,1.0,11)

# solution by solve_ivp
Y1=solve_ivp(f1,[0,1],[0],t_eval=t1)
Y2=solve_ivp(f2,[2.0,3.0],[1.0],t_eval=t2)
Y3=solve_ivp(f3,[1,2],[2.0],t_eval=t3)
Y4=solve_ivp(f4,[0,1],[1.0],t_eval=t4)

#finding derivative to verify solution
d1=np.gradient(Y1.y[0],Y1.t,edge_order=2)
d2=np.gradient(Y2.y[0],Y2.t,edge_order=2)
d3=np.gradient(Y3.y[0],Y3.t,edge_order=2)
d4=np.gradient(Y4.y[0],Y4.t,edge_order=2)

#comparing derivatives with f(x,y)
pt.subplot(2,2,1)
pt.plot(Y1.t,d1,'m:',label='dy/dx')
pt.plot(Y1.t,f1(Y1.t,Y1.y[0]),'c--',label='f(x,y)')
pt.xlabel("x");pt.ylabel("Dy")
pt.title("eqn 1")
pt.legend()
pt.subplot(2,2,2)
pt.plot(Y2.t,d2,'m:',label='dy/dx')
pt.plot(Y2.t,f2(Y2.t,Y2.y[0]),'c--',label='f(x,y)')
pt.xlabel("x");pt.ylabel("Dy")
pt.title("eqn 2")
pt.legend()
pt.subplot(2,2,3)
pt.plot(Y3.t,d3,'m:',label='dy/dx')
pt.plot(Y3.t,f3(Y3.t,Y3.y[0]),'c--',label='f(x,y)')
pt.xlabel("x");pt.ylabel("Dy")
pt.title("eqn 3")
pt.legend()
pt.subplot(2,2,4)
pt.plot(Y4.t,d4,'m:',label='dy/dx')
pt.plot(Y4.t,f4(Y4.t,Y4.y[0]),'c--',label='f(x,y)')
pt.xlabel("x");pt.ylabel("Dy")
pt.title("eqn 4")
pt.legend()
pt.tight_layout()
pt.savefig('/media/jibak/Data/JIBAK/GS/Computational physics/Assignment 2/A2_7_1.png')
pt.clf()

# plotting solutions 
pt.subplot(2,2,1)
pt.plot(Y1.t ,Y1.y[0],'b:^',label="Numeric solution")
pt.plot(t1,e1(t1),'k-',label='Exact solution')
pt.title("Equation 1")
pt.legend()
pt.subplot(2,2,2)
pt.plot(Y2.t ,Y2.y[0],'g:.',label='Numeric solution')
pt.plot(t2,e2(t2),'k-',label="Exact solution")
pt.title("Equation 2")
pt.legend()
pt.subplot(2,2,3)
pt.plot(Y3.t ,Y3.y[0],'r:o',label='Numeric solution')
pt.plot(t3,e3(t3),'k-',label="Exact solution")
pt.title("Equation 3")
pt.legend()
pt.subplot(2,2,4)
pt.plot(Y4.t ,Y4.y[0],'m:s',label='Numeric solution')
pt.plot(t4,e4(t4),'k-',label="Exact solution")
pt.title("Equation 4")
pt.legend()
pt.show()
