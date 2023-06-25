import math
import matplotlib.pyplot as plt
maxpoints=1000
t=[ ]
y=[ ]
dx=0.01
w0=5;
for point_count in range(maxpoints):
    tp=point_count*dx
    t.append(tp)
    y.append(math.sin(w0*tp))
plt.plot(t,y)
plt.xlabel('t value (sec)')
plt.ylabel('y value')
plt.savefig('plot.png')