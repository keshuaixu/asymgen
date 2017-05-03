#!/usr/bin/env python3

import rospy
from asymgen.msg import heatherwave
from geometry_msgs.msg import WrenchStamped
import numpy as np


def normalize(val, gain=1):
    return -1 + (2 / (1 + np.exp(-gain * val)))


class Force2Wave:
    def __init__(self):
        rospy.init_node('force2wave')
        rospy.Subscriber('wrench', WrenchStamped, self.wrench_callback)
        self.wave_pub_x = rospy.Publisher('wave_x', heatherwave, queue_size=10)
        self.wave_pub_y = rospy.Publisher('wave_y', heatherwave, queue_size=10)
        self.wave_pub_z = rospy.Publisher('wave_z', heatherwave, queue_size=10)
        self.amp_x, self.amp_y, self.amp_z = (0, 0, 0)
        rospy.Timer(rospy.Duration(1/40), self.timer_callback)

    def wrench_callback(self, w):
        force = w.wrench.force
        self.amp_x, self.amp_y, self.amp_z = normalize(np.array([force.x, force.y, force.z]), gain=1000)

    def timer_callback(self, evt):
        hold_width = 0.007
        slope_width = 0.025
        repeat = 1
        wave_x = heatherwave(amplitude=self.amp_x, hold_width=hold_width, slope_width=slope_width, repeat=repeat)
        wave_y = heatherwave(amplitude=self.amp_y, hold_width=hold_width, slope_width=slope_width, repeat=repeat)
        wave_z = heatherwave(amplitude=self.amp_z, hold_width=hold_width, slope_width=slope_width, repeat=repeat)
        self.wave_pub_x.publish(wave_x)
        self.wave_pub_y.publish(wave_y)
        self.wave_pub_z.publish(wave_z)


force2wave = Force2Wave()

while not rospy.is_shutdown():
    rospy.spin()
