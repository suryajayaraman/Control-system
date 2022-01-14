import control
import numpy as np
import math
from control.matlab import *
import matplotlib.pyplot as plt


''' example transfer function to test the step response'''
##num = [1]
##den = [1,2,5]
##sys = tf(num, den)
##pole(sys)
##
#### the poles of the transfer function are same as the eigen values of the
#### state transition matrix A
##[A,B,C,D] = ssdata(sys)
##eigen = np.linalg.eig(A)
##eigen_values = eigen[0]
##eigen_vector = eigen[1]


'''
DC Gain
The DC gain, $k_{dc}$, is the ratio of the magnitude of the steady-state step response to the magnitude of the step input.
For stable transfer functions, the Final Value Theorem demonstrates that the DC gain is the value of the transfer function evaluated at s = 0.
For first-order systems of the forms shown, the DC gain is $k_{dc} = b/a$.

Time Constant
The time constant of a first-order system is $T_c = \tau = 1/a$ which is equal to the time it takes for the system
response to reach 63% of its steady-state value for a step input (from zero initial conditions) or to decrease to 37% of the initial value
for a systems free response. More generally, it represents the time scale for which the dynamics of the system are significant.
'''


##Step response of first order system
##k_dc = 5
##Tc = 10
##u = 2
##
##G = tf( [k_dc], [ Tc, 1])
##
##plt.figure(1)
##result = step(u*G)
##plt.plot(result[1], result[0], 'b-')
##plt.title('Step repsone of first order system')
##plt.show()
##
##
##plt.figure(2)
##bode(G)
####plt.title('Bode plots of first order system')
##plt.show()


'''Second order system response'''
'''
DC Gain
The DC gain, k_{dc}, again is the ratio of the magnitude of the steady-state step response to the magnitude of the step input, and for stable systems
it is the value of the transfer function when $s = 0$. For the forms given,
##k_{dc} = 1 / {k}

Damping Ratio
The damping ratio zeta is a dimensionless quantity charaterizing the rate at which an oscillation in the system's response decays due to effects such as
viscous friction or electrical resistance. From the above definitions,
##zeta = {b} / {2 *sqrt{k m}

Natural Frequency
The natural frequency omega_n is the frequency (in rad/s) that the system will oscillate at when there is no damping, zeta = 0
##omega_n = 1/ sqrt{{k*m}}

Poles/Zeros
The canonical second-order transfer function has two poles at:
##s_p = -\zeta \omega_n \pm j \omega_n \sqrt{1-\zeta^2}

Underdamped Systems

If $\zeta < 1$, then the system is underdamped. In this case, both poles are complex-valued with negative real parts; therefore,
the system is stable but oscillates while approaching the steady-state value. Specifically, the natural response oscillates with the damped natural frequency,
omega_d = omega_n / sqrt{1-\zeta^2} (in rad/sec).
'''


##underdamped system response
k_dc = 1
w_n = 10
zeta = 0.2

underdamped_second_order_system = tf( [(k_dc * w_n**2)], [1, 2*w_n * zeta, w_n**2])

####pole zero map
##plt.figure(1)
##pzmap(underdamped_second_order_system)

#### step response
##plt.figure(2)
##result = step(underdamped_second_order_system)
##plt.plot(result[1], result[0], 'b-')
##plt.title('Step repsone of underdamped_second_order_system')
##plt.show()


##overdamped second order system response
k_dc = 1
w_n = 10
zeta = 1.2

overdamped_second_order_system = tf( [(k_dc * w_n**2)], [1, 2*w_n * zeta, w_n**2])

####pole zero map
##plt.figure(1)
##pzmap(overdamped_second_order_system)
##
#### step response
##plt.figure(2)
##result = step(overdamped_second_order_system)
##plt.plot(result[1], result[0], 'b-')
##plt.title('Step repsone of Overdamped second_order_system')
##plt.show()


##critically damped second order system response
k_dc = 1
w_n = 10
zeta = 1.0

critically_damped_second_order_system = tf( [(k_dc * w_n**2)], [1, 2*w_n * zeta, w_n**2])

####pole zero map
##plt.figure(1)
##pzmap(critically_damped_second_order_system)
##
#### step response
##plt.figure(2)
##result = step(critically_damped_second_order_system)
##plt.plot(result[1], result[0], 'b-')
##plt.title('Step repsone of critically damped second_order_system')
##plt.show()



##undamped second order system response
k_dc = 1
w_n = 10
zeta = 0.0

undamped_second_order_system = tf( [(k_dc * w_n**2)], [1, 2*w_n * zeta, w_n**2])

####pole zero map
##plt.figure(1)
##pzmap(undamped_second_order_system)
##
####step response
##plt.figure(2)
##result = step(undamped_second_order_system)
##plt.plot(result[1], result[0], 'b-')
##plt.title('Step repsone of undamped_second_order_system')
##plt.show()

bode(underdamped_second_order_system, overdamped_second_order_system, critically_damped_second_order_system, undamped_second_order_system)
plt.figure(1)
plt.legend(['underdamped: zeta < 1','overdamped: zeta > 1','critically-damped: zeta = 1','undamped: zeta = 0'])
plt.show()
