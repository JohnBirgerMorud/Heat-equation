import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation, PillowWriter


nrows = 50
ncols = 50
time  = 100

# u = np.zeros(time*nrows*ncols).reshape(time, nrows, ncols)
u = np.zeros(time*nrows*ncols).reshape(time, nrows, ncols)

def f0(list):
    #list = np.random.rand(nrows, ncols)
    center = int(len(list[0])/2)
    print(center)
    
    q = int(center/2)
    list[center-q : (center+q) , center-q: (center+q)] = 1

    return list

## Program

u[0] = f0(u[0])

#print(u[0])

##Konstanter
K = 0.1

#print(len(u))


for t in range(time-1):
    for x in range(1, nrows-1):
        for y in range(1, ncols-1):
            
            ###Eksplisitt løsning.
            q_opp = u[t][x-1][y+1] + u[t][x][y+1] + u[t][x+1][y+1] - 3*u[t][x][y]
            q_ned = u[t][x-1][y-1] + u[t][x][y-1] + u[t][x+1][y-1] - 3*u[t][x][y]
            q_hor = u[t][x-1][y] + u[t][x+1][y] - 2*u[t][x][y] 
            
            u[t+1][x][y] = u[t][x][y] + K * (q_opp+q_hor+q_ned)


def update(frame):
    plt.clf()
    plt.imshow(u[frame], cmap='viridis', interpolation='none')
    plt.title(f'Time Step: {frame}')
    plt.colorbar()

# Create the animation
fig = plt.figure()
animation = FuncAnimation(fig, update, frames=time, repeat=False)

# Save the animation as a GIF
writer = PillowWriter(fps=5)
animation.save('diffusion_animation.gif', writer=writer)

# Display the animation (optional)
#plt.show()

