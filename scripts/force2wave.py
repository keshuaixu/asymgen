import rospy
from asymgen.msg import heatherwave
from geometry_msgs.msg import WrenchStamped

class Force2Wave:
    def __init__(self):
        rospy.init_node('force2wave')
        rospy.Subscriber('force2wave/wrench', WrenchStamped, self.wrench_callback)
        self.wave_pub = rospy.Publisher('force2wave/wave', heatherwave)

    def wrench_callback(self):
        pass
