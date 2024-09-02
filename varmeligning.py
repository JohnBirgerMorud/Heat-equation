import matplotlib.pyplot as plt
import numpy as np

nrows = 100
ncols = 100

u = np.zeros(nrows*ncols).reshape(nrows, ncols)

def f0(list):
    for i in range(len(list)):
        #x_i = np.pi / (len(list)-1) * i
        #list[i] = np.sin(x_i)
        
        list[i] = 1 / (len(list)-1) * i


## Program
## Setter startverdiene til en sinus

f0(u[0])

##Konstanter
k = 0.1
h = 1
K = 0.1
kh = 0.4
#print(len(u))


for t in range(len(u)-1):
    for x in range(2, len(u[t])-2):
        
        #u[t+1][x] = u[t][x] + 0.5 * (u[t][x+1] - 2*u[t][x] + u[t][x-1]) 
        est_n = u[t][x] + kh * (u[t][x+1] - 2*u[t][x] + u[t][x-1])
        est_np1 = u[t][x+1] + kh * (u[t][x+2] - 2*u[t][x+1] + u[t][x])
        est_nm1 = u[t][x-1] + kh * (u[t][x] - 2*u[t][x-1] + u[t][x-2])
        
        # Implisitt:
        #u[t+1][x] = u[t][x] + K * (est_np1 - 2 * est_n + est_nm1)
        u[t+1][x] = u[t][x] + K * ((u[t][x+1] - 2*u[t][x] + u[t][x-1]) + (est_np1 - 2 * est_n + est_nm1))

#print(u[-1][-1])

#print(u[0] - u[5])
#plt.imshow(u)
plt.pcolormesh(u)
plt.show()