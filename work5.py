
import math
import sympy as sp
from mpmath import ln


def derivative(f,x):
    my_f1=sp.diff(f,x)
    return sp.lambdify(x, my_f1)


def newtonraphson(fun,eps,start,end):
    itr=0
    x = sp.symbols('x')
    F = sp.lambdify(x, fun)
    f= derivative(fun, x)

    i=start
    while(i<end):
        if(F(i)*F(i+1)<=0):
            x0=(i*2+1)/2
            xr=i+1
            error =( -(ln((eps) / (i+1-i))/ln(2)))



            while((abs(xr-x0)>eps)and(error>itr)):
                if f(x0)==0:
                    print("cant divided by zero")
                    return

                temp=xr
                xr=x0-(F(x0)/f(x0))
                x0=temp
                itr=itr+1
            print("itr",itr,"root:",xr)
            itr=0
        i=i+1

def secant_method(fun,eps,start,end):
    itr=0
    x = sp.symbols('x')
    F = sp.lambdify(x, fun)  # פונקציה מקורית\
    i=start
    while(i<end):
        if(F(i)*F(i+1)<=0):
            x0=(i*2+1)/2
            x1=i+1
            xr=x1
            error =( -(ln((eps) / (i+1-i))/ln(2)))



            while((abs(x1-x0)>eps)and(error>itr)):
                if (F(x1)-F(x0))==0:
                    print("cant divided by zero")
                    return

                temp=xr
                xr=(x0*F(x1)-x1*F(x0))/(F(x1)-F(x0))
                x1=xr
                x0=temp

                itr=itr+1
            print("itr",itr,"root:",xr)
            itr=0
        i=i+1




x = sp.symbols('x')
f =x**3-x-1
newtonraphson(f,0.00001,-10,10)
secant_method(f,0.00001,-10,10)





