import numpy as np
from numba import jit
import matplotlib.pyplot as plt
from time import time
start = time()

nx = 1800  #main figure x resolution
ny = 1200  #main figure y resolution

jx = 1800  #Julia rendering x res
jy = 1800   #Julia rendering y res

#number of iterations of the Mandelbrot set calculation
iters = 100
#number of iterations of the Julia sets calculation
iters_j = 100

colormap = 'hot_r'    #chosen colormap

#x and y limits  of the main figure
ext = [-2,1,-1.15,1.15]
#x and y limits of the Julia rendering
ext_j = [-2,2,-2,2]

@jit
def iterative(n,z,c):
    for i in range(n):
        if abs(z) < 2:
            z = z*z + c
        else: break
    return i;

def mandelbrot(x,y,nx,ny):
    z = complex(0,0)
    escape = np.zeros([nx,ny])
    for nx_index, re in enumerate(x):
        for ny_index, im in enumerate(y):
            c = complex(re,im)
            escape[nx_index,ny_index] = iterative(iters,z,c)
        if nx_index % 100 == 0:
            print('%.2f'%(nx_index/nx))
    return escape;

def julia(xx,yy,jx,jy,c):
    getaway = np.zeros([jx,jy])
    for jx_index, re in enumerate(xx):
        for jy_index, im in enumerate(yy):
            z = complex(re,im)
            getaway[jx_index,jy_index] = iterative(iters,z,c)
        if jx_index % 100 == 0:
            print('%.2f'%(jx_index/jx))
    return getaway;


def render_julia(c):

    start = time()

    fig1 = plt.figure(1)
    plt.clf()

    xx = np.linspace(ext_j[0],ext_j[1],jx)
    yy = np.linspace(ext_j[2],ext_j[3],jy)

    getaway = julia(xx,yy,jx,jy,c)

    plt.imshow(getaway.T,cmap=colormap,extent=ext_j,origin='lower')
    plt.title(r'$%.2f$ $%.2f$i'%(c.real,c.imag), fontsize = 'medium')

    #plt.imsave(fname=r'###path###',arr=getaway.T,cmap=colormap,,extent=ext_j,origin='lower')

    print('\n')
    print(time() - start)
    print('\n')

    plt.show()


def onclick(event):

    cx = event.xdata
    cy = event.ydata

    c = complex(cx,cy)

    render_julia(c)

x = np.linspace(ext[0],ext[1],nx)
y = np.linspace(ext[2],ext[3],ny)

escape = mandelbrot(x,y,nx,ny)

fig0 = plt.figure(0)

plt.imshow(escape.T,cmap=colormap,extent=ext,origin='lower')

#plt.imsave(fname=r'###path###',arr=escape.T,cmap=colormap,extent=ext,origin='lower')

print('\n')
print(time() - start)
print('\n')

cid0 = fig0.canvas.mpl_connect('button_press_event', onclick) 

plt.show()

