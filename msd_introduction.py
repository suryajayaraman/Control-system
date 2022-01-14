import control
import numpy as np
import math
from control.matlab import *
import matplotlib.pyplot as plt


##MSD system state space representation
##states are position and velocity
m = 1.0
k = 1.0
b = 0.2
F = 1.0

##state space form representation
A = np.array([
    [0,1],
    [-k/m, -b/m]
    ])

B = np.array([[0], [1/m]])

C = np.array([[1, 0]])
D = [0]

sys = ss(A,B,C,D)
##Continuous-time transfer function.



##transfer function representation
num = [1]
den = [m , b, k]
tf_system = tf(num, den)
print( type(tf_system))



''' Example of conversions between models '''
num = [2 ,1]
den = [4, 3, 2]
G = tf(num,den)
print(G)
print('state space form of the transfer function is ')

##ssdata(G)
[A,B,C,D] = ssdata(G)
H = ss(A,B,C,D)


## zeros, poles and gains conversion
## 'v' returns vectorized version of the zeros and poles, which is useful for SISO systems.
a = pzmap(tf_system, Plot =True, title = ' Pole zero map')
##print(type(a)) tuple is the output
pole(tf_system)
zero(tf_system)
plt.show()
