import math

def func(x):
    return x**4+4*x**3-6*x**2-9*x-1
def ljb(x):
    return 16*x**3+12*x**2-12*x-9
def lkb(x):
    return 48*x**2+24*x-12
def fwe(a,b,eps):
        if ljb(b)*lkb(b)>0:
            x=b
        else:
            x=a
        print(x)
        h=func(x) / ljb(x)
        x=x-h
        if abs(h) <= eps:
            f=ljb(b)
            print(x,func(x))
        else:
            h=func(x) / ljb(x)
            x=x-h
fwe(-1, 0.75, 0.001)
fwe(0.75, 2,0.001)