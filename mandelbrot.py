import numpy as np
import matplotlib.pyplot as plt
import time
plt.rcParams['axes.facecolor'] = 'k'
start = time.time()

nx = 600
ny = 400
iters = 35
size = 0.7

def iterative(n,z,c):
    for i in range(n):
        if abs(z) < 2:
            z = z*z + c
        else: break
    return z,i;

x = np.linspace(-2,1,nx)
y = np.linspace(-1.15,1.15,ny)
xx = xx1 = xx2 = xx3 = xx4 = xx5 = np.array([])
yy = yy1 = yy2 = yy3 = yy4 = yy5 = np.array([])

for nx, re in enumerate(x):
    for ny, im in enumerate(y):
        z = complex(0,0)
        c = complex(re,im)
        ignore, escape = iterative(iters,z,c)
        if 0<=escape<iters/12:
            xx5 = np.append(xx5,re)
            yy5 = np.append(yy5,im)
        if iters/12<=escape<iters/8:
            xx4 = np.append(xx4,re)
            yy4 = np.append(yy4,im)
        if iters/8<=escape<iters/3:
            xx3 = np.append(xx3,re)
            yy3 = np.append(yy3,im)
        if iters/3<=escape<2*iters/3:
            xx2 = np.append(xx2,re)
            yy2 = np.append(yy2,im)
        if 2*iters/3<=escape<iters-1:
            xx1 = np.append(xx1,re)
            yy1 = np.append(yy1,im)
        if escape == iters-1:
            xx = np.append(xx,re)
            yy = np.append(yy,im)

plt.errorbar(xx,yy,color='k',fmt='.',markersize=size)
plt.errorbar(xx1,yy1,color='y',fmt='.',markersize=size)
plt.errorbar(xx2,yy2,color='w',fmt='.',markersize=size)
plt.errorbar(xx3,yy3,color='b',fmt='.',markersize=size)
plt.errorbar(xx4,yy4,color='darkblue',fmt='.',markersize=size)
plt.errorbar(xx5,yy5,color='k',fmt='.',markersize=size)

print('\n')
print(time.time() - start)
plt.show()
plt.rcParams['axes.facecolor'] = 'w'
