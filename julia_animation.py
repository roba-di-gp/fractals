import numpy as np
from numba import jit
import matplotlib as mpl
mpl.use('tkagg')
import matplotlib.pyplot as plt
import matplotlib.animation as anim
from time import time
start = time()

#parameter space
sp = [0,2*np.pi]

#number of frames
num = 100

#interval between frames
interval = 30

def fc(p):
#define c as function of p
    c = 0.7885*np.exp(p*1j)
    return c

@jit
def map(z,c):
#define the polynomial map
    return z*z + c

#x and y limits of the main figure
xlim, ylim = 1.7,1.7
ext = [-xlim,xlim,-ylim,ylim]

jx = 300  #Julia rendering x res
jy = 300 #Julia rendering y res

#number of iterations
iters = 100

#colormap
colormap = 'inferno'

@jit
def iterative(n,z,c):
    for i in range(n):
        if abs(z) < 2:
            z = map(z,c)
        else: break
    return i;

def julia(xx,yy,jx,jy,c):
    getaway = np.zeros([jx,jy])
    for jx_index, re in enumerate(xx):
        for jy_index, im in enumerate(yy):
            z = complex(re,im)
            getaway[jx_index,jy_index] = iterative(iters,z,c)
    return getaway;

x = np.linspace(ext[0],ext[1],jx)
y = np.linspace(ext[2],ext[3],jy)

fig = plt.figure()

ims = []

par = np.linspace(sp[0],sp[1],num)

for p_index, p in enumerate(par):

    c = fc(p)

    getaway = julia(x,y,jx,jy,c)

    im=plt.imshow(getaway.T,cmap=colormap,interpolation='bilinear',extent=ext,origin='lower', animated=True)

    ims.append([im])

    if p_index % 10 == 0:
        print('%.2f'%(p_index/num))

video = anim.ArtistAnimation(fig, ims, interval=interval, repeat_delay=0, blit=True)

writer = anim.PillowWriter(fps=60)

#video.save(r'###path###\filename.gif',writer= writer)

plt.show()
