#!/usr/bin/env python3
import numpy as np
import sounddevice as sd

from wavegen import heather_wave, asymmetric_sine
from asymgen.msg import heatherwave

# import curses
# import os
import argparse
# import pprint
import rospy

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--device', type=int, nargs=1)
parser.add_argument('-c', '--channel', type=int, nargs=1)
parser.add_argument('-wh', '--hold-width', type=float, nargs=1, default=[0.03])
parser.add_argument('-ws', '--slope-width', type=float, nargs=1, default=[0.02])
parser.add_argument('-a', '--amplitude', type=float, nargs=1, default=[1.0])
parser.add_argument('-r', '--direction', type=float, nargs=1, default=1)
parser.add_argument('-q', '--query-devices', action='store_true')

args, unknown = parser.parse_known_args()

if args.query_devices:
    print(sd.query_devices())
    exit()


class AsymGenNode:
    def __init__(self, args_):
        rospy.init_node('wave2sound')
        if args_.device is not None:
            self.output_device = args_.device[0]
        else:
            self.output_device = sd.default.device
        self.device_info = sd.query_devices(device=self.output_device, kind='output')
        self.args = args_
        rospy.Subscriber('wave', heatherwave, self.heather_callback)

    def heather_callback(self, msg):
        s = heather_wave(hold_width=msg.hold_width, slope_width=msg.slope_width,
                         amplitude=msg.amplitude, direction=1)
        samples = np.vstack(
            (s if ch == self.args.channel[0] else np.zeros(s.size) for ch in
             range(self.device_info['max_output_channels']))).transpose()
        sd.play(np.tile(samples, (msg.repeat, 1)), 44100, blocking=False, loop=False, device=self.output_device)

    
print(args)

asymgennode = AsymGenNode(args)

while not rospy.is_shutdown():
    rospy.spin()
sd.stop()

#
#
# def curses_main(win):
#     win.nodelay(True)
#     win.nodelay(True)
#     key = ''
#     win.clear()
#     win.addstr(pprint.pformat(asymgennode.device_info))
#     while 1:
#         try:
#             key = win.getkey()
#             if str(key) == 'q':
#                 break
#
#             # win.addstr(str(key))
#             if str(key) == ',':
#                 direction = -1
#             if str(key) == '.':
#                 direction = 1
#
#             s = heather_wave(hold_width=args.hold_width[0], slope_width=args.slope_width[0],
#                              amplitude=args.amplitude[0], direction=direction)
#             samples = np.vstack(
#                 (s if ch == args.channel[0] else np.zeros(s.size) for ch in
#                  range(device_info['max_output_channels']))).transpose()
#             sd.play(np.tile(samples, (10, 1)), 44100, blocking=True, loop=False, device=args.device[0])
#
#
#
#
#         except KeyboardInterrupt:
#             break
#         except Exception as e:
#             # No input
#             pass
#
#
# curses.wrapper(curses_main)
