# asymgen
asymmetric haptic feedback function generator with sound card

# requirements

Python 3.6
virtualenv

# install
clone it into your `catkin_ws/src`
```
cd asymgen
virtualenv venv -p python3.6
source venv/bin/activate
pip install -r requirements.txt
```
```bash
cd ~/catkin_ws
catkin_make
```

# run
Only -d and -c are actually used. Other parameters come from the message.
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

# topics
`asymgen/out/0`
`asymgen/out/1`
`...`
depending on the audio channel.

message type `heatherwave`

# test message
```bash
rostopic pub /asymgen/out/0 asymgen/heatherwave "amplitude: 1.0
hold_width: 0.05
slope_width: 0.05
repeat: 10" 
```
You should be able to hear clicks

# todo
launch file

create another node to convert from force to heatherwave
