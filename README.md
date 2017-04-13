# asymgen
asymmetric haptic feedback function generator with sound card

# requirements

Python 3.6
virtualenv

# install
```
cd asymgen
virtualenv venv -p python3.6
source venv/bin/activate
pip install -r requirements.txt
```

# run
```
usage: python asymgen.py [-h] [-d DEVICE] [-c CHANNEL] [-wh HOLD_WIDTH]
                  [-ws SLOPE_WIDTH] [-a AMPLITUDE] [-r DIRECTION]

optional arguments:
  -h, --help            show this help message and exit
  -d DEVICE, --device DEVICE
  -c CHANNEL, --channel CHANNEL
  -wh HOLD_WIDTH, --hold-width HOLD_WIDTH
  -ws SLOPE_WIDTH, --slope-width SLOPE_WIDTH
  -a AMPLITUDE, --amplitude AMPLITUDE
  -r DIRECTION, --direction DIRECTION

```
use <kbd>,</kbd> and <kbd>.</kbd> to generate waveform.
