#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 16:48:59 2017

@author: endo
"""

import rospy
#from std_msgs.msg import Float32MultiArray
from sensor_msgs.msg import LaserScan
import matplotlib.pyplot as plt
#import matplotlib.animation as animation
import math 
import numpy as np

def map_vals(dist_vals):
#    plt.cla() 
        print(dist_vals.ranges)

def listener():
    rospy.init_node('Mapper', anonymous=True)
    rospy.Subscriber('scan', LaserScan, map_vals)
    rospy.spin()

angles=np.arange(0.0, 2*math.pi,2*math.pi/1440)

#if __name__ == '__main__':
try:		
      print("Mapping node started ")
      listener()
except rospy.ROSInterruptException:
      print('crashed')
      pass