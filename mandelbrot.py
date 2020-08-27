import numpy as np
import matplotlib.pyplot as plt
import time
start = time.time()

nx = 900
ny = 600
iters = 25

def f(z,c):
    return z*z + c

x = np.linspace(-2,1,nx)
y = np.linspace(-1,1,ny)
xx = np.array([])
yy = np.array([])

for i in range(nx):
    for j in range(ny):
        z = complex(0,0)
        for n in range(iters):
            if abs(z) < 2:
                z = f(z,complex(x[i],y[j]))
            else: break
        if abs(z) < 2:
            xx = np.append(xx,x[i])
            yy = np.append(yy,y[j])
    if i % 10 == 0:
        print('%.2f'%(i/nx))

plt.errorbar(xx,yy,color='black',fmt='.',markersize=0.32)

print('\n')
print(time.time() - start)
plt.show()
