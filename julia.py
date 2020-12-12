import numpy as np
from numba import jit
import matplotlib.pyplot as plt
from time import time
start = time()

c = 0.1+0.618033j   #constant term of the polynomial map

@jit
def map(z):
    #define the polynomial map
    return z*z + c

jx = 1800  #Julia rendering x res
jy = 1800   #Julia rendering y res

#number of iterations of the Julia sets calculation
iters = 100

colormap = 'hot_r'  #chosen colormap

#x and y limits of the main figure
ext = [-2,2,-2,2]

rx,ry = 0.06,0.06 #x and y zoom radii

@jit
def iterative(n,z,c):
    for i in range(n):
        if abs(z) < 2:
            z = map(z)
        else: break
    return i;

def julia(xx,yy,jx,jy,c):
    getaway = np.zeros([jx,jy])
    for jx_index, re in enumerate(xx):
        for jy_index, im in enumerate(yy):
            z = complex(re,im)
            getaway[jx_index,jy_index] = iterative(iters,z,c)
        if jx_index % 100 == 0:
            print('%.2f'%(jx_index/jx))
    return getaway;

def zoom(xp,yp,rx,ry):

    start = time()

    fig1 = plt.figure(1)
    plt.clf()

    ext1 = [xp-rx,xp+rx,yp-ry,yp+ry]
    x = np.linspace(ext1[0],ext1[1],jx)
    y = np.linspace(ext1[2],ext1[3],jy)

    getaway = julia(x,y,jx,jy,c)

    plt.imshow(getaway.T,cmap=colormap,extent=ext1,origin='lower')
    plt.title(r'$[%.2f,%.2f]{\times}[%.2f,%.2f]$'%(ext1[0],ext1[1],ext1[2],ext1[3]), fontsize = 'medium')

    #plt.imsave(fname=r'###path###',arr=getaway.T,cmap=colormap,extent=ext1,origin='lower')

    print('\n')
    print(time() - start)
    print('\n')

    plt.show()

def onclick(event):

    xp = event.xdata
    yp = event.ydata

    zoom(xp,yp,rx,ry)

x = np.linspace(ext[0],ext[1],jx)
y = np.linspace(ext[2],ext[3],jy)

getaway = julia(x,y,jx,jy,c)

fig0 = plt.figure(0)

plt.imshow(getaway.T,cmap=colormap,extent=ext,origin='lower')

#plt.imsave(fname=r'###path###',arr=escape.T,cmap=colormap,extent=ext,origin='lower')

print('\n')
print(time() - start)
print('\n')

cid0 = fig0.canvas.mpl_connect('button_press_event', onclick)

plt.show() 
