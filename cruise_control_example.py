# -*- coding: cp1252 -*-
import control
import numpy as np
import math
from control.matlab import *
import matplotlib.pyplot as plt



m = 1000
b = 50

A = -b/m
B = 1/m
C = 1
D = 0

##state space form and tf of the cruise control model
cruise_ss = ss(A,B,C,D)
cruise_tf = tf([1], [m, b])

##Performance criteria
'''
When the engine gives a 500 Newton force, the car will reach a maximum velocity of 10 m/s (22 mph),
see open-loop step response section below. An automobile should be able to accelerate up to that speed in less than 5 seconds.
In this application, a 10% overshoot and 2% steady-state error on the velocity are sufficient.

Keeping the above in mind, we have proposed the following design criteria for this problem:

Rise time < 5 s
Overshoot < 10%
Steady-state error < 2%
'''

#reference output to be tracked
r = 10
t = np.linspace(0, 20, 20*11)
u = 500

'''open loop performance analysis'''
##result = step( u* cruise_tf)
##plt.plot(result[1], result[0], 'b-')
##plt.title('Step repsone of cruise control open-loop system')
####plt.show()
##
##plt.figure(2)
##pzmap(cruise_tf)
##plt.title('Pole-zero map of cruise control open-loop system')
####plt.show()
##
##plt.figure(3)
##plt.title('Bode plot of cruise control open-loop system')
##bode(cruise_tf)
##plt.show()





'''proportional integral controller'''
##kp = 100
##p_controller_cruise = tf([kp], [m, (b + kp)])
##result = step( r* p_controller_cruise, t)
##plt.plot(result[1], result[0], 'b-')
##plt.axis([0, 20, 0, 10])
##plt.figure(3)
##plt.title('Step rsesponse of 1D P controller kp = 100')
##plt.show()
##
##kp = 5000
##p_controller_cruise2 = tf([kp], [m, (b + kp)])
##result = step( r* p_controller_cruise2, t)
##plt.figure(4)
##plt.plot(result[1], result[0], 'r-')
##plt.title('Step rsesponse of 1D P controller kp = 5000')
##plt.show()

'''
conclusion:

##The steady-state error is now essentially zero, and the rise time has been reduced substantially. However, this response is unrealistic because
##a real cruise control system generally can notchange the speed of the vehicle from 0 to 10 m/s in less than 0.5 seconds
##due to power limitations of the engine and drivetrain.


Problems:
1. steady state error
2. rise time is larger
'''


'''proportional integral controller '''
kp = 800
ki = 30
pi_controller_cruise = tf([kp, ki], [m, (b + kp), ki])
##pi_zeros, pi_poles = zero(pi_controller_msd_system), pole(pi_controller_msd_system)
plt.figure(5)
result = step( r* pi_controller_cruise, t)
plt.plot(result[1], result[0], 'g-')
plt.title('Step response of 1D PI controller kp = 500 and ki = 5')
plt.show()



####proportional integral derivative controller
##kp = 350
##ki = 300
##kd = 50
##
##pid_controller_msd_system = tf([kd, kp, ki], [m, (b + kd), (k +kp), ki])
##pid_zeros, pid_poles = zero(pid_controller_msd_system), pole(pid_controller_msd_system)
##plt.figure(2)
##result = step(pid_controller_msd_system)
##plt.plot(result[1], result[0], 'c-')
##plt.title('Step response of 1D PID controller kp = 300 ,ki = 10 and kd =')
##plt.show()




####proportional derivative controller
##kp = 300
##kd = 10
##pd_controller_msd_system = tf([kd, kp], [m, (b + kd), (k + kp)])
##pd_zeros, pd_poles = zero(pd_controller_msd_system), pole(pd_controller_msd_system)
##plt.figure(2)
##result = step(pd_controller_msd_system)
##plt.plot(result[1], result[0], 'r-')
##plt.title('Step rsesponse of 1D PD controller kp = 300 and kd = 10')
##
##

