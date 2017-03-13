import numpy as np
import sounddevice as sd

from wavegen import heather_wave, asymmetric_sine

s = heather_wave(hold_width=0.01, slope_width=0.02, amplitude=1, direction=1)
s2 = asymmetric_sine()

samples = np.vstack((s2, np.zeros(s2.size))).transpose()
sd.play(samples, 44100, blocking=False, loop=True, mapping=[1, 2], device=3)
sd.wait()
