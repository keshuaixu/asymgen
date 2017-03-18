import numpy as np


def asymmetric_sine(frequency=20, amplitude=1, direction=1, asymmetricity=0, sample_rate=44100):
    x = np.linspace(0, 2 * np.pi, num=np.round(sample_rate / frequency))
    omega1 = np.pi * (1 + 0.5 * asymmetricity)
    omega2 = np.pi * (1 - 0.5 * (1 - asymmetricity))
    y1 = -np.cos(x * np.pi / omega1)
    y2 = -np.cos(x * np.pi / omega2)
    return np.where(x < omega1, y1, y2) * amplitude * direction


def heather_wave(hold_width=0.02, slope_width=0.03, amplitude=1, direction=1, sample_rate=44100):
    samples_hold = np.repeat(1, hold_width * sample_rate)
    samples_slope = np.linspace(1, 0, num=slope_width * sample_rate)
    return np.hstack(([0], samples_hold, samples_slope, [0])) * amplitude * direction
    # return np.hstack((samples_hold, samples_slope)) * amplitude * direction