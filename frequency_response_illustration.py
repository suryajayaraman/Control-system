# -*- coding: cp1252 -*-
import control
import numpy as np
import math
from control.matlab import *
import matplotlib.pyplot as plt

system  = tf( [50], [1, 9,30, 40])
##bode(system)
##phase margin is about 100 degrees

gain = 100
gsystem = system * gain
##plt.figure(2)
##bode(gsystem)


gm1, pm1, wg1, wp1 = margin(system)
gm2, pm2, wg2, wp2 = margin(gsystem)
##The phase plot is exactly the same as before, and the magnitude plot is shifted up by 40 dB (gain of 100)
##The phase margin is now about -60 degrees.
## the wgc or the gain crossover frequency doesnt change as the phase plot doesnt change


'''
gm (float) – Gain margin
pm (float) – Phase margin (in degrees)
wg (float) – Frequency for gain margin (at phase crossover, phase = -180 degrees)
wp (float) – Frequency for phase margin (at gain crossover, gain = 1)
Margins are calculated for a SISO open-loop system.
If there is more than one gain crossover, the one at the smallest
margin (deviation from gain = 1), in absolute sense, is
returned. Likewise the smallest phase margin (in absolute sense)
is returned.
'''


'''
Bandwidth Frequency
The bandwidth frequency is defined as the frequency at which the closed-loop magnitude drops 3 dB below its magnitude at DC (magnitude as the frequency approaches 0).
However, when we design via frequency response, we are interested in predicting the closed-loop behavior from the open-loop response.
Therefore, we will use a second-order system approximation and say that the bandwidth frequency equals the frequency at which the open-loop magnitude response is
between -6 and -7.5 dB, assuming the open-loop phase response is between -135 deg and -225 deg. 

In order to illustrate the importance of the bandwidth frequency, we will show how the output changes with different input frequencies.
We will find that sinusoidal inputs with frequency less than $\omega_{bw}$ (the bandwidth frequency) are tracked "reasonably well" by the system.
Sinusoidal inputs with frequency greater than $\omega_{bw}$ are attenuated (in magnitude) by a factor of 0.707 or greater (and are also shifted in phase).

'''
## the closed-loop transfer function representing a system:
G  = tf( [1], [1, 0.5, 1])
plt.figure(1)
bode(G)
plt.title(' Bode plot')


##this is the closed-loop transfer function, our bandwidth frequency will be the frequency corresponding to a gain of -3 dB 1.4 rad/s.
##for an input frequency of 0.3 radians, the output sinusoid should have a magnitude about one and the phase should be shifted by perhaps a few degrees (behind the input).
##For an input frequency of 3 rad/sec, the output magnitude should be about -20 dB (or 1/10 as large as the input) and the phase should be nearly -180 (almost exactly out-of-phase).

## first input of frequency 0.3 rad/s
w = 0.3
t = np.linspace(0, 100, 10100 )
u = np.sin(w * t)
yout, T, xout  = lsim(G,u,t)
plt.figure(2)
plt.plot(t,u , 'b')
plt.title('time response for w = 0.3 rad/s')
plt.hold(True)
plt.plot(t, yout , 'r')
plt.axis([50, 100, -2, 2])



## first input of frequency 0.3 rad/s
w = 3.0
t = np.linspace(0, 100, 10100 )
u = np.sin(w * t)
yout, T, xout  = lsim(G,u,t)
plt.figure(3)
plt.plot(t,u , 'b')
plt.title('time response for w = 3 rad/s')
plt.hold(True)
plt.plot(t, yout , 'r')
plt.axis([50, 100, -2, 2])
plt.show()
