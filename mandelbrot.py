import numpy as np
import matplotlib.pyplot as plt
from numba import jit
import time
start = time.time()

nx = 3000
ny = 2000
iters = 60

z = complex(0,0)

@jit
def iterative(n,z,c):
    for i in range(n):
        if abs(z) < 2:
            z = z*z + c
        else: break
    return i;

x = np.linspace(-2.05,1,nx)
y = np.linspace(-1.2,1.2,ny)
escape = np.zeros([nx,ny])

for nx_index, re in enumerate(x):
    for ny_index, im in enumerate(y):
        c = complex(re,im)
        escape[nx_index,ny_index] = iterative(iters,z,c)
    if nx_index % 10 == 0:
        print('%.2f'%(nx_index/nx))

plt.imshow(escape.T,cmap='hot',extent=[-2.2,1,-1.1,1.1])

print(time.time() - start)
plt.show()

