import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation, PillowWriter
from scipy import integrate

nrows = 10
ncols = 10
time  = 10

B = 1
H = 1

u = np.zeros(time*nrows*ncols).reshape(time, nrows, ncols)

def g(x,y):
    return np.sin(np.pi/B * x)*np.sin(np.pi/H * y)

def A(n,m):
    f0 = np.sin(np.pi/B * x)*np.sin(np.pi/H * y)
    f = lambda y,x: f0 *np.sin(n*np.pi/B*x)*np.sin(m*np.pi/H*y)
    s =  integrate.dblquad(f, 0, B, 0, H, epsabs=1e-3)[0]
    #print("doneA")
    return 4/(B*H) * s

def T(x,y,t, counter):
    s = 0
    for n in range(1,10):
        for m in range(1,10):
            lam = (n*np.pi/B)**2 - (m*np.pi/H)**2
            s += A(n,m) * np.sin(n*np.pi/B * x) * np.sin(m*np.pi/H * y) * np.exp(lam * t)
    
    counter +=1
    print(counter)
    return s, counter
    
c = 0
for t in range(len(u)):
    for y in range(len(u[t])):
        for x in range(len(u[t][y])):
            u[t][y][x], c = T(x,y,t, c)

## Animation

def update(frame):
    plt.clf()
    plt.imshow(u[frame], cmap='viridis', interpolation='none')
    plt.title(f'Time Step: {frame}')
    plt.colorbar()

# Create the animation
fig = plt.figure()
animation = FuncAnimation(fig, update, frames=time, repeat=False)

# Save the animation as a GIF
writer = PillowWriter(fps=1)
animation.save('diffusion_animation.gif', writer=writer) 

# Display the animation (optional)
#plt.show()

