import numpy as np
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

def int_CR3BPn(X,t,u):
	### Position vectors and magnitues
	r1 = np.array([X[0]+u, X[1], X[2]])
	r2 = np.array([X[0]+u-1, X[1], X[2]])
	r1_mag = np.linalg.norm(r1)
	r2_mag = np.linalg.norm(r2)

	### Equations of Motion
	ddx = 2*X[4] + X[0] - (1-u)*(X[0]+u)/(r1_mag**3) - u*(X[0]+u-1)/(r2_mag**3);
	ddy = -2*X[3] + X[1] -((1-u)/(r1_mag**3) + u/(r2_mag**3))*X[1];
	ddz = -((1-u)/(r1_mag**3) + u/(r2_mag**3))*X[2];

	### Assigning output states
	v = np.array([X[3], X[4], X[5]])
	a_CR3BP = np.array([ddx, ddy, ddz])
	
	dXdt = np.hstack([v, a_CR3BP])

	return dXdt

# Constants
MR_Europa  = 2.528133998624693e-05
Rn_Europa  = 0.002325733869766
Rn_Jupiter = 0.104173744598421

# ICs
r0n = [1.0204617015266166,-0.0012084061620286,0.0000000000000000]
v0n = [-0.0028596241729016,0.0009291482175995,0.0000000000000000]

X0n = np.hstack([r0n, v0n])

### Time

timen = np.linspace(0,6.94118,10000)


X = odeint(int_CR3BPn, X0n, timen, args = (MR_Europa,))



fig, ax = plt.subplots() # note we must use plt.subplots, not plt.subplot
# (or if you have an existing figure)
# fig = plt.gcf()
# ax = fig.gca()
plt.plot(X[:,0],X[:,1],'b',label='orbit',color='red')
circ_Europa = plt.Circle((1-MR_Europa,0),Rn_Europa,edgecolor='black',facecolor='blue')
plt.legend(loc='best')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()
ax.add_artist(circ_Europa)

plt.show()
