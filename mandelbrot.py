import numpy as np
import matplotlib.pyplot as plt
import time
plt.rcParams['axes.facecolor'] = 'k'
start = time.time()

nx = 600
ny = 400
iters = 35

def f(z,c):
    return z*z + c

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

for i in range(nx):
    for j in range(ny):
        z = complex(0,0)
        c = complex(x[i],y[j])
        ignore, escape = iterative(iters,z,c)
        if 0<=escape<iters/12:
            xx5 = np.append(xx5,x[i])
            yy5 = np.append(yy5,y[j])
        if iters/12<=escape<iters/8:
            xx4 = np.append(xx4,x[i])
            yy4 = np.append(yy4,y[j])
        if iters/8<=escape<iters/3:
            xx3 = np.append(xx3,x[i])
            yy3 = np.append(yy3,y[j])
        if iters/3<=escape<2*iters/3:
            xx2 = np.append(xx2,x[i])
            yy2 = np.append(yy2,y[j])
        if 2*iters/3<=escape<iters-1:
            xx1 = np.append(xx1,x[i])
            yy1 = np.append(yy1,y[j])
        if escape == iters-1:
            xx = np.append(xx,x[i])
            yy = np.append(yy,y[j])
    if i % 10 == 0:
        print('%.2f'%(i/nx))

plt.errorbar(xx,yy,color='k',fmt='.',markersize=0.8)
plt.errorbar(xx1,yy1,color='y',fmt='.',markersize=0.8)
plt.errorbar(xx2,yy2,color='w',fmt='.',markersize=0.8)
plt.errorbar(xx3,yy3,color='b',fmt='.',markersize=0.8)
plt.errorbar(xx4,yy4,color='darkblue',fmt='.',markersize=0.8)
plt.errorbar(xx5,yy5,color='k',fmt='.',markersize=0.8)

print('\n')
print(time.time() - start)
plt.show()
plt.rcParams['axes.facecolor'] = 'w'
