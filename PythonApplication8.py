import math
import numpy as np
x=[1.5,2.0,2.5,3.0,3.5,4.0]
y=[10.517,10.193,9.807,9.387,8.977,8.637]
h=x[1]-x[0]
def func(y,j):
	mas=[]
	for i in range(len(y)):
    		mas.append(y[i]-y[i-1])
    		mas.pop(0)
	if j == 1 :
		return mas
	else:
		j-=1
	return func(mas,j)
	return mas
	print(func(y,j))
#yx1=1/h*func(y,1)[1]-func(y,2)[1]/2+func(y,3)[1]/3-func(y,4)[1]/4
#yx2=1/h**2*func(y,2)[1]-func(y,3)[1]+11/12*func(y,4)[1]
#print(yx1)
#print(yx2)
