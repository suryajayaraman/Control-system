#!/usr/bin/env python
import pandas as pd
import numpy as np
import math
##import can
##import rospy
from wabco_msgs import path_tracking_cmd
from std_msgs.msg import String

#initialising parameters
lat_err_previous = 0.0
curr_lat_err = 0.0
heading_err_previous = 0.0
curr_heading_err = 0.0

#vehicle parameters
wheel_base = 2.5
steering_ratio = 19.5

#can parameters
GPS_GMC_message_id = '0xffffff'
bus = can.interface.Bus(bustype='pcan', channel='PCAN_USBBUS1', bitrate=250000)

#gains tuning 
K_p_lateral = 2.0
K_d_lateral = 0.1
''''''
K_p_heading = 0.6
K_d_heading = 0.1
''''''
feed_fwd_curvature_gain = 0.6


'''subscriber to get lateral, heading offsets and curvature, send GPS1_GMC CAN message '''
def set_errors(data):
    
    global curr_heading_err, curr_lat_err, heading_err_previous, lat_err_previous
    curr_lat_err = data.lateral_Offset
    curr_heading_err = data.heading_Offset
    lat_err_grad      = ( curr_lat_err - lat_err_previous ) / 0.2
    heading_err_grad  = ( curr_heading_err - heading_err_previous ) / 0.2
    print('curr_lat_err is \n'     + str(curr_lat_err))
    print('curr_heading_err is \n' + str(curr_heading_err))
    
    #feedforward term
    delta_ff = data.curvature
    print('curvature is \n' + str(curvature))
    
    #feedback term
    delta_fb = (K_p_lateral * curr_lat_err)     + (K_d_lateral * lat_err_grad) +
               (K_p_heading * curr_heading_err) + (K_d_heading * heading_err_grad)
    print('feedback demand is \n' + str(delta_fb))
    
    total_delta = (delta_ff + delta_fb) * -1000.0
    print('Total curvature demand is \n' + str(total_delta)) 

    #print total_calculated steering wheel angle and curvature demand
    curvature_input  = total_delta / 1000.0 '''total curvature demand'''
    steering_angle   = np.atan2(curvature_input * wheel_base) * steering_ratio
    print('Total steering_angle demand is \n' + str(steering_angle))
    print(':) ------- :) ------- :) ------- :) ------- :) ------- \n')
    
    #GPS1_GMC_CAN_message #applying curvature cmd message offset and factor
    total_delta = () *    
    hex_data = str() + str() + ''
    msg = can.Message(arbitration_id=0xc0ffee, data=[0, 25, 0, 1, 3, 1, 4, 1], extended_id=True)     
    bus.send(msg)
    
    #re-setting errors
    lat_err_previous     = curr_lat_err
    heading_err_previous = curr_heading_err


def get_error():
    rospy.init_node('path_control_listener', anonymous=True)
    rospy.Subscriber("/path_control", path_tracking_cmd, set_errors)
    rospy.spin()  # spin() simply keeps python from exiting until this node is stopped


if __name__ == '__main__':
    get_error()


#mmi vsp publishers to EHSU - 2 publishers
    
###publisher
##def talker():
##    pub = rospy.Publisher('chatter', String, queue_size=10)
##    rospy.init_node('talker', anonymous=True)
##    rate = rospy.Rate(10) # 10hz
##    while not rospy.is_shutdown():
##        hello_str = "hello world %s" % rospy.get_time()
##        rospy.loginfo(hello_str)
##        pub.publish(hello_str)
##        rate.sleep()
##
##def send_one():
##    bus = can.interface.Bus(bustype='pcan', channel='PCAN_USBBUS1', bitrate=250000)
##    #bus = can.interface.Bus(bustype='ixxat', channel=0, bitrate=250000)
##    #bus = can.interface.Bus(bustype='vector', app_name='CANalyzer', channel=0, bitrate=250000)
##
##    msg = can.Message(arbitration_id=0xc0ffee,
##                      data=[0, 25, 0, 1, 3, 1, 4, 1],
##                      extended_id=True)
##    try:
##        bus.send(msg)
##        print("Message sent on {}".format(bus.channel_info))
##    except can.CanError:
##        print("Message NOT sent")
