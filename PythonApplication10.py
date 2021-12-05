import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
from numpy import *
x = [1.2, 1.4, 1.7, 2.3, 2.8]
y = [1.36, 1.15, 2.34, 0.92, 3.12]
spl = UnivariateSpline(x, y)
xs = linspace(1.2, 2.8, 2000)
plt.plot(x,y,'ro',xs, spl(xs), 'g')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Lab. work №10')
plt.grid()
plt.show()
