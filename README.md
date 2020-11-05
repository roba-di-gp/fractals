# Fractal world

[julia_sets_in_mandelbrot]

A super-simple escape time algorithm is implement to render the Mandelbrot set for a chosen complex polynomial map, in a specified Python colormap. Click on a point *(x,y)* on the main figure to render the filled-in Julia set for the same polynomial map of fixed constant term *c = x +iy*.

mandelbrot_explorer

The same method as above is used to render the Mandelbrot set. Click on a point *(x,y)* to render his neighborhood of width *2rx* and height *2ry*.

julia_explorer

The program renders the filled-in Julia set for a chosen polynomial map through an escape time algorithm. Click on a point *(x,y)* to render his neighborhood of width *2rx* and height *2ry*.

burning_ship_explorer

The method of the previous programs is implemented to render the Burning ship fractal. Click on a point *(x,y)* to zoom on his neighborhooh.

juia_animation

Animate a sequence of filled-in Julia sets. The sequence of the complex constants *c* is obtained through a specified function *c = fc(p)* defined on the parameter space *sp*. The *c*s are plugged in a polynomial map that is iterated *iters* times to render the sequence of frames of the animation.
