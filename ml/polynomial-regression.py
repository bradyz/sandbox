import numpy as np
import pylab as pl

# make sure points are not really random
np.random.seed(42)

# array of 20 random points
x = np.random.random(20)
y = np.sin(2 * x)

# linear regression of y with respect to x
p_1 = np.polyfit(x, y, 1)
p_2 = np.polyfit(x, y, 2)

# values
xfit = np.linspace(0, 1, 1000)
yfit = np.polyval(p_1, xfit)
y1fit = np.polyval(p_2, xfit)

# axis and config
pl.scatter(x, y, c='k')
pl.xlabel('x')
pl.ylabel('y')

pl.plot(xfit, np.sin(2 * xfit))
pl.plot(xfit, yfit)
pl.plot(xfit, y1fit)

pl.show()
