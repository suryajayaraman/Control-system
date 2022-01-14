# -*- coding: cp1252 -*-
import control
import numpy as np
import math
from control.matlab import *
import matplotlib.pyplot as plt


m = 1
b = 10
k = 20

sys = tf([1], [ m, b, k])

Ts = 1/100.0
sys_d = c2d(sys,Ts,'zoh')
