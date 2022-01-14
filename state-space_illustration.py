# -*- coding: cp1252 -*-
import control
import numpy as np
import math
from control.matlab import *
import matplotlib.pyplot as plt

A= np.array([
    [0, 1,0 ],
    [980, 0, -2.8],
    [0, 0, -100]
    ])

B = np.array([
    [0], [0], [100]
    ])

C = np.array([1, 0, 0])


t = np.linspace(0, 2, 202)
## zero input condition
u = np.zeros(t.shape)
##initial state vector
x0 = [0.01, 0, 0]

sys = ss(A,B,C,0)

##y,t,x = lsim(sys,u,t,x0)
##plt.plot(t,y, 'b')
##plt.title('Open-Loop Response to Non-Zero Initial Condition')
##plt.xlabel('Time (sec)')
##plt.ylabel('Ball Position (m)')
##plt.show()

##It looks like the distance between the ball and the electromagnet will go to infinity,
##but probably the ball hits the table or the floor first
##(and also probably goes out of the range where our linearization is valid).

'''Controllability and Observability'''
##A system ($A$, $B$) is controllable if and only if a system ($A'$, $B'$) is observable.

 
ctrb_rank = np.linalg.matrix_rank(control.ctrb(A,B))
obsb_rank = np.linalg.matrix_rank(control.obsv(A,C))


##control.gram(sys, 'c')
##ValueError: Oops, the system is unstable!



p1 = -10 + 10j
p2 = -10 - 10j
p3 = -50

K = place(A,B,[p1, p2, p3])
sys_cl = ss(A-B*K,B,C,0)

y,t,x = lsim(sys_cl,u,t,x0)
plt.figure(2)
plt.plot(t,y, 'b')
plt.xlabel('Time (sec)')
plt.ylabel('Ball Position (m)')
plt.title(' -10 +- 10j and -50 poles result')
##plt.show()


p1 = -30 + 30j
p2 = -30 - 30j
p3 = -50

K = place(A,B,[p1, p2, p3])
sys_cl = ss(A-B*K,B,C,0)
plt.figure(3)
y,t,x = lsim(sys_cl,u,t,x0)
plt.plot(t,y, 'b')
plt.xlabel('Time (sec)')
plt.ylabel('Ball Position (m)')
plt.title(' -30 +- 30j and -50 poles result')
plt.show()

