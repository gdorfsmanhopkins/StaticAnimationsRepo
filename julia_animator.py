#This program will turn a parameterized path in the complex plane into an animation of the frames of the associated julia sets.

from PIL import Image
import numpy as np

#Image width and height in pixels:
width, height = 500, 500

#The number of frames we'd like
num_frames = 100

#The domain of the parameterization of our path in the complex plane
path_start = 0
path_end = 3.14159
path_length = path_end-path_start
step_size = path_length/(num_frames)


#This function is a parameterized path through the complex plane.
#Play with this (and the domain) to make different julia set deformations.
#Right now it traverses the upper half of the main cardioid of the Mandlebrot set (counterclockwise)
def path(t):
    x = .5*np.cos(t)*(1-np.cos(t))+.25
    y = .5*np.sin(t)*(1-np.cos(t))
    c = complex(x,y)
    return c

#This function makes a pixel matrix for the julia set associated to the complex function z^2+c
#We adapted it from "Learning Scientific Programming with Python" by Chris Hill
#See https://scipython.com/book/chapter-7-matplotlib/problems/p72/the-julia-set/
def julia_matrix_maker(c,real_min = -1.5,real_max=1.5,imag_min=-1.5,imag_max=1.5,max_iter=50,radius=2):
    real_range = real_max-real_min
    imag_range = imag_max-imag_min

    #Initialize our pixel matrix as all white.
    julia_pixels = np.array([[255]*width for i in range(height)])

    #Now we go through every pixel, and figure out what color to draw it
    for i in range(width):
        for j in range(height):
            #Which complex number x+iy is in the (i,j) pixel?
            x = (real_min + (i/width)*real_range)
            y = (imag_min + (j/height)*imag_range)
            z = complex(x,y)

            #Now we iterate z^2 + c.
            iteration = 0
            while iteration < max_iter:
                z = z**2 + c

                #If we ever leave the circle of the given radius, we're not in the Julia set so we color the pixel black
                if abs(z)>radius:
                    julia_pixels[j][i] = 0
                    break
                iteration += 1

    #We've now populated the pixel matrix.  Let's return it.
    return julia_pixels

#This loop makes and saves all the frames
for i in range(num_frames+1):
    print("Working on frame",i)
    t = path_start + step_size*i

    #Get the pixel matrix associated to our point on the path and cast it to a matrix of bytes
    pixel_matrix = np.uint8(julia_matrix_maker(path(t)))

    #Use PIL to convert the matrix of bytes into a grayscale image (for us black and white)
    im = Image.fromarray(pixel_matrix)

    #Save it
    pathname = f"./juliaStack/julias_{1000+i}.png"
    im.save(pathname)
