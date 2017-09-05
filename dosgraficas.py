import numpy as np
import pylab as pl
x=[5000, 6000, 7000, 8000, 9000]
y=[65, 78, 88, 89, 93]
pl.plot(x, y)
x1=[7000, 8000, 9000, 10000, 11000]
y1=[65, 75, 85, 86, 98]
pl.plot(x1, y1)
pl.xlabel('Voltaje [y]')
pl.ylabel('Eficiencia [x]')
pl.savefig('temp1.png')
