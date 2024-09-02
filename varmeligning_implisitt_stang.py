import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Definere konstanter

L = 1
n = 20
dx = L/n

m = 500
dt = 1
t = dt*m


def setMatrix(n):
    A = np.zeros(n*n)
    counter = 0

    for i in range(n):
        for j in range(n):
            idx = i*n + j
            
            if idx == (j*n + i):
                A[idx] = 2

            elif idx == (i*n + 1 + i) or idx == (i*n - 1 + i):
                A[idx] = -1

    A.resize(n, n)
    return A



A = setMatrix(n)
u0 = np.zeros(n)
for i in range(len(u0)):
    u0[i] = np.sin(np.pi*L/(n-1) *i)


### Solve

u = u0


fig, ax = plt.subplots()
x_vals = np.linspace(0, L, n)
line, = ax.plot(x_vals, u0)

def update(frame):
    global u
    t = frame * dt
    Q = np.identity(n) + t * A
    u = np.linalg.solve(Q, u0)
    line.set_ydata(u)
    return line,

num_frames = m

# Create the animation
ani = FuncAnimation(fig, update, frames=num_frames, interval=50, blit=True)

# Save the animation as a GIF
ani.save('heat_equation_animation.gif', writer='imagemagick', fps=10)
