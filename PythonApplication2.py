import math

def func(x):
    return x**4+4*x**3-6*x**2-9*x-1
def ljb(x):
    return 16*x**3+12*x**2-12*x-9
def lkb(x):
    return 48*x**2+24*x-12
def combine(a,b,eps):
    condition = True
    if ljb(b)*lkb(b):
        a0=b
        b0=a
    else:
        a1=a
        b1=b
        xp1=a1
        xp2=b1
    while condition:
        xn1=xp1-f(xp1)*(xp2-xp1)
        