# StaticAnimationsRepo
A repository for the Static Animations workshop at Construct3D 2023

flowerStack contains the frames of the polar flower animation we will all do together.
flower_animator.py is the python file which created those frames.
flowerSurface.stl is the completed 3D model build from these frames.

juliaStack contains the frames of a Julia set deformation/animation.
julia_animator.py is the python file which created those frames.

alpha_remover.py is a python script which will import images, and remove the alpha layer, and export them.  This is necessary for PNGs with alpha layers, as chimera will not be able to open files with alpha layers.  flower_animator.py and julia_animator.py already remove alpha layers, so it isn't necessary to do in those instances.
