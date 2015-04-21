import numpy as np
import pylab as pl

np.random.seed(42)
x = np.random.random(20)
y = np.sin(2 * x)
p = np.polyfit(x, y, 1)

x_p = np.random.random(3)
y_p = np.polyval(p, x_p)

xfit = np.linspace(0, 1, 1000)
yfit = np.polyval(p, xfit)
pl.scatter(x, y, c='k')
pl.xlabel('x')
pl.ylabel('y')
pl.plot(xfit, yfit)

pl.show()
