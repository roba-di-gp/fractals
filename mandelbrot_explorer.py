import numpy as np
import matplotlib.pyplot as plt
from numba import jit
import time
start = time.time()

nx = 1800  #x resolution
ny = 1200 #y resolution
iters = 100   #number of iterations

colormap = 'binary'    #chosen colormap

ext = [-2,1,-1.15,1.15]   #x and y limits  of the main figure

rx, ry = 0.036,0.024 #x and y zoom radii

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

def zoom(xp,yp,rx,ry):

    start = time.time()

    fig1 = plt.figure(1)
    plt.clf()

    ext1 = [xp-rx,xp+rx,yp-ry,yp+ry]
    x = np.linspace(ext1[0],ext1[1],nx)
    y = np.linspace(ext1[2],ext1[3],ny)

    escape = mandelbrot(x,y,nx,ny)

    plt.imshow(escape.T,cmap=colormap,extent=ext1,origin='lower')
    plt.title(r'$[%.2f,%.2f]{\times}[%.2f,%.2f]$'%(ext1[0],ext1[1],ext1[2],ext1[3]), fontsize = 'medium')

    #plt.imsave(fname=r'c:\users\gugli\desktop\roba\mandelpy_zoom4.jpg',arr=escape.T,cmap=colormap,origin='lower')

    print('\n')
    print(time.time() - start)
    print('\n')

    plt.show()

def onclick(event):

    xp = event.xdata
    yp = event.ydata

    zoom(xp,yp,rx,ry)

x = np.linspace(ext[0],ext[1],nx)
y = np.linspace(ext[2],ext[3],ny)

escape = mandelbrot(x,y,nx,ny)

fig0 = plt.figure(0)

plt.imshow(escape.T,cmap=colormap,extent=ext,origin='lower')

#plt.imsave(fname=r'###path###',arr=escape.T,cmap=colormap,extent=ext,origin='lower')

print('\n')
print(time.time() - start)
print('\n')

cid0 = fig0.canvas.mpl_connect('button_press_event', onclick)

plt.show()


