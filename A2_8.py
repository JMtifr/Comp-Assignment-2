# Assignment 2
# Problem 8
#y'=p
#y"=p'
from scipy.integrate import solve_bvp
import numpy as np
import matplotlib.pyplot as pt

# defining f(x,[y])
def f1(x,y):
 return (np.vstack((y[1], -np.exp(-2.0*y[0]))))
def f2(x,y):
 return(np.vstack((y[1],np.cos(x)*y[1]-y[0]*np.log(y[0]))))
def f3(x,y):
 return(np.vstack((y[1],-(2.0*y[1]**3+y[0]**2*y[1])/np.cos(x))))
def f4(x,y):
 return(np.vstack((y[1],0.5-y[1]**2/2.0-y[0]*np.sin(x)/2.0)))

# defining boundary conditions
def bc1(ya,yb):
 return np.array([yb[0]-np.log(2),ya[0]])
def bc2(ya,yb):
 return (np.array([ya[0]-1.0,yb[0]-np.exp(1)]))
def bc3(ya,yb):
 return(np.array([ya[0]-2.0**(-0.25),yb[0]-12.0**0.25/2.0]))
def bc4(ya,yb):
 return(np.array([ya[0]-2.0,yb[0]-2.0]))

# creating x arrays
x1=np.linspace(1.0,2.0,11)
x2=np.linspace(0.0,np.pi/2.0,17)
x3=np.linspace(np.pi/4.0,np.pi/3.0,14)
x4=np.linspace(0.0,np.pi,32)

#creating initial solutions
y1=np.zeros((2,x1.size))+1.0
y2=np.zeros((2,x2.size))+1.0
y3=np.zeros((2,x3.size))+1.0
y4=np.zeros((2,x4.size))+1.0

# Finding solutions using solve_bvp
Y1=solve_bvp(f1,bc1,x1,y1)
Y2=solve_bvp(f2,bc2,x2,y2)
Y3=solve_bvp(f3,bc3,x3,y3)
Y4=solve_bvp(f4,bc4,x4,y4)

# finding derivative of solution to check correctness
d1=np.gradient(Y1.y[0],Y1.x,edge_order=2); dd1=np.gradient(d1,Y1.x,edge_order=2)
d2=np.gradient(Y2.y[0],Y2.x,edge_order=2); dd2=np.gradient(d2,Y2.x,edge_order=2)
d3=np.gradient(Y3.y[0],Y3.x,edge_order=2); dd3=np.gradient(d3,Y3.x,edge_order=2)
d4=np.gradient(Y4.y[0],Y4.x,edge_order=2); dd4=np.gradient(d4,Y4.x,edge_order=2)


# comparing derivative and y"
pt.subplot(2,2,1)
pt.plot(x1,dd1,'c--',label="differentiation")
pt.plot(x1,f1(x1,[Y1.y[0],dd1])[1],'m:',label="f(x,y,dy/dx)")
pt.xlabel("x");pt.ylabel("D2y")
pt.title("Eqn 1")
pt.legend()
pt.subplot(2,2,2)
pt.plot(x2,dd2,'c--',label="differentiation")
pt.plot(x2,f2(x2,[Y2.y[0],d2])[1],'m:',label="f(x,y,dy/dx)")
pt.xlabel("x");pt.ylabel("D2y")
pt.title("Eqn 2")
pt.legend()
pt.subplot(2,2,3)
pt.plot(Y3.x,dd3,'c--',label="differentiation")
pt.plot(Y3.x,f3(Y3.x,[Y3.y[0],d3])[1],'m:',label="f(x,y,dy/dx)")
pt.xlabel("x");pt.ylabel("D2y")
pt.title("Eqn 3")
pt.legend()
pt.subplot(2,2,4)
pt.plot(Y4.x,dd4,'c--',label="differentiation")
pt.plot(Y4.x,f4(Y4.x,[Y4.y[0],d4])[1],'m:',label="f(x,y,dy/dx)")
pt.xlabel("x");pt.ylabel("D2y")
pt.title("Eqn 4")
pt.legend()
pt.tight_layout()
pt.savefig('/media/jibak/Data/JIBAK/GS/Computational physics/Assignment 2/A2_8_1.png')
pt.clf()

#plotting solutions
pt.subplot(2,2,1)
pt.plot(Y1.x,Y1.y[0],'b:',label='numerical')
pt.title("Eqn 1 solution")
pt.xlabel("x");pt.ylabel("y")
pt.legend()

pt.subplot(2,2,2)
pt.plot(Y2.x,Y2.y[0],'r:',label='numerical')
pt.title("Eqn 2 solution")
pt.xlabel("x");pt.ylabel("y")
pt.legend()
pt.subplot(2,2,3)
pt.plot(Y3.x,Y3.y[0],'m:',label='numerical')
pt.title("Eqn 3 solution")
pt.xlabel("x");pt.ylabel("y")
pt.legend()
pt.subplot(2,2,4)
pt.plot(Y4.x,Y4.y[0],'c:',label='numerical')
pt.title("Eqn 4 solution")
pt.xlabel("x");pt.ylabel("y")
pt.legend()
pt.tight_layout()
pt.show()
