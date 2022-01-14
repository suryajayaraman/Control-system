import control
import numpy as np
import math
from control.matlab import *
import matplotlib.pyplot as plt



##MSD system state space representation
##states are position and velocity
m = 1.0
b = 10.0
k = 20.0
F = 1.0


##transfer function representation
##Continuous-time transfer function.
##msd_system = tf([1], [m, b, k])
##plt.figure(1)
##result = step(msd_system)
##plt.plot(result[1], result[0], 'b-')
##plt.title('Step response of 1D open loop Mass spring damper system')


##proportional  controller
kp = 300
p_controller_msd_system = tf([kp], [m, b, (k + kp)])
p_zeros, p_poles = zero(p_controller_msd_system), pole(p_controller_msd_system)
plt.figure(2)
result = step(p_controller_msd_system)
plt.plot(result[1], result[0], 'b-')
plt.title('Step rsesponse of 1D P controller kp = 300')



##proportional derivative controller
kp = 300
kd = 10
pd_controller_msd_system = tf([kd, kp], [m, (b + kd), (k + kp)])
pd_zeros, pd_poles = zero(pd_controller_msd_system), pole(pd_controller_msd_system)
plt.figure(2)
result = step(pd_controller_msd_system)
plt.plot(result[1], result[0], 'r-')
plt.title('Step rsesponse of 1D PD controller kp = 300 and kd = 10')


##proportional integral controller
kp = 30
ki = 50
pi_controller_msd_system = tf([kp, ki], [m, b, (k +kp), ki])
pi_zeros, pi_poles = zero(pi_controller_msd_system), pole(pi_controller_msd_system)
plt.figure(2)
result = step(pi_controller_msd_system)
plt.plot(result[1], result[0], 'g-')
plt.title('Step response of 1D PD controller kp = 300 and ki = 10')



##proportional integral derivative controller
kp = 350
ki = 300
kd = 50

pid_controller_msd_system = tf([kd, kp, ki], [m, (b + kd), (k +kp), ki])
pid_zeros, pid_poles = zero(pid_controller_msd_system), pole(pid_controller_msd_system)
plt.figure(2)
result = step(pid_controller_msd_system)
plt.plot(result[1], result[0], 'c-')
plt.title('Step response of 1D PID controller kp = 300 ,ki = 10 and kd =')
plt.show()

plt.figure(3)
control.root_locus(pid_controller_msd_system)
plt.show()
