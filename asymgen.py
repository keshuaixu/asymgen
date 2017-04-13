import numpy as np
import sounddevice as sd

from wavegen import heather_wave, asymmetric_sine

import curses
import os
import argparse
import pprint

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--device', type=int, nargs=1)
parser.add_argument('-c', '--channel', type=int, nargs=1)
parser.add_argument('-wh', '--hold-width', type=float, nargs=1, default=[0.03])
parser.add_argument('-ws', '--slope-width', type=float, nargs=1, default=[0.02])
parser.add_argument('-a', '--amplitude', type=float, nargs=1, default=[1.0])
parser.add_argument('-r', '--direction', type=float, nargs=1, default=1)

args = parser.parse_args()

device_info = sd.query_devices(device=args.device[0], kind='output')

print(args)


def curses_main(win):
    win.nodelay(True)
    key = ''
    win.clear()
    win.addstr(pprint.pformat(device_info))
    while 1:
        try:
            key = win.getkey()
            if str(key) == 'q':
                break

            # win.addstr(str(key))
            if str(key) == ',':
                direction = -1
            if str(key) == '.':
                direction = 1

            s = heather_wave(hold_width=args.hold_width[0], slope_width=args.slope_width[0],
                             amplitude=args.amplitude[0], direction=direction)
            samples = np.vstack(
                (s if ch == args.channel[0] else np.zeros(s.size) for ch in
                 range(device_info['max_output_channels']))).transpose()
            sd.play(np.tile(samples, (10, 1)), 44100, blocking=True, loop=False, device=args.device[0])




        except KeyboardInterrupt:
            break
        except Exception as e:
            # No input
            pass


curses.wrapper(curses_main)
sd.stop()
