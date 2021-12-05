import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
from numpy import *
#first example
x = [2.1, 2.7, 2.8, 2.9, 3.0, 3.1]
y = [2.5, 2.77, 2.94, 3.11, 3.29, 3.47]

#second example
x = [1.4, 1.6, 1.9, 2, 2.1, 2.2]
y = [2.5, 2.70, 3, 3.27, 3.56, 3.92]

spl = UnivariateSpline(x, y)
xs = linspace(1.5, 3.1, 2000)
plt.plot(x,y,'go',xs, spl(xs), 'y')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Lab. work №14')
plt.grid()
plt.show()
