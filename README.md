# asymgen
asymmetric haptic feedback function generator with sound card

# requirements

Python 3.6
virtualenv

# install

Don't forget to source your ros **and** catkin workspace `setup.bash`

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

```bash
 roslaunch asymgen dvrk_haptic_asym.launch 
```

# topics
`wave2sound0/wave`
`wave2sound1/wave`

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
