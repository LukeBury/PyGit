import numpy as np
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def int_2BI(X,t,u):
	r = np.array([X[0], X[1], X[2]])
	r_mag = np.linalg.norm(r)

	a_2B = r*(-u / (r_mag**3))

	v = np.array([X[3], X[4], X[5]])

	
	dXdt = np.hstack([v, a_2B])
	'''
	dXdt = [v, a_2B]
	'''
	return dXdt


# Constants
R_Earth = 6378 # km
u_Earth = 398600.4415

# ICs
r0 = [R_Earth+500, 0, 0]
v0 = [0, 7.612683986157750, 0]


X0 = np.hstack([r0, v0])
'''
X0 = [r0, v0]
'''
print X0
### Time
'''
t0 = 0
tf = 90*60
dt = 10
time = np.arange(t0, tf+dt, dt)
'''
time = np.linspace(0,95*60,1000)

print len(time)

X = odeint(int_2BI, X0, time, args = (u_Earth,))

'''
plt.plot(t, sol[:, 0], 'b', label='theta(t)')
plt.plot(t, sol[:, 1], 'g', label='omega(t)')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.show()
'''

plt.plot(X[:,0],X[:,1],'b',label='orbit')
plt.legend(loc='best')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()
plt.show()


'''
d = np.array([1, 2, 3, 1, 1])
d_mag = np.linalg.norm(d)
print(d_mag)
print d*2
'''
