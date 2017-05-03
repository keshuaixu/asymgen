# asymgen
asymmetric haptic feedback function generator with sound card

# requirements

Ubuntu 16.04

ROS kinetic

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
