import numpy as np
from scipy.sparse import diags
from scipy.sparse.linalg import spsolve
import matplotlib.pyplot as plt


# Parameters
L = 1.0        # Length of the square
Nx = 5        # Number of spatial grid points in x
Ny = 5        # Number of spatial grid points in y
Nt = 100       # Number of time steps
alpha = 0.01   # Thermal diffusivity

# Discretization
dx = float(L / (Nx - 1))
dy = float(L / (Ny - 1))
dt = 0.001    # You might need to adjust this for stability

# Initial condition
u0 = np.zeros((Nx, Ny))
u0[1:4, 1:4] = 1.0  # Initial square of temperature

# Create sparse matrix for the implicit Euler scheme
Ax = diags([1, -2, 1], [-1, 0, 1], shape=(Nx, Nx), format='csr') / dx**2
Ay = diags([1, -2, 1], [-1, 0, 1], shape=(Ny, Ny), format='csr') / dy**2



# Initialize A matrix with zeros
A = np.zeros((Nx * Ny, Nx * Ny))


# Fill A matrix using explicit loops
for i in range(1, Nx - 1):
    for j in range(1, Ny - 1):
        idx = i * Ny + j
        print(idx)
        A[idx, idx] = 1 + 2 * alpha * dt * (1 / dx**2 + 1 / dy**2)
        A[idx, idx - 1] = A[idx, idx + 1] = -alpha * dt / dx**2
        A[idx, idx - Ny] = A[idx, idx + Ny] = -alpha * dt / dy**2
        
A = A[1:-1, 1,-1]
print(A)

""" 
# Time-stepping
u = u0.flatten()
for t in range(Nt):
    print(f"A: {np.shape(A)}, u: {np.shape(u)}")

    print(t)
    print(f"A: {A}, \nu: {u}")
    u = spsolve(A, u)

# Reshape the flattened solution back to 2D
u_final = u.reshape((Nx, Ny))

# Plot the final solution
plt.imshow(u_final, extent=[0, L, 0, L], origin='lower', cmap='viridis', interpolation='none')
plt.colorbar(label='Temperature')
plt.title('Heat Equation - Implicit Euler')
plt.xlabel('x')
plt.ylabel('y')
plt.show() """
