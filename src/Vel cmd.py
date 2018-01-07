import rospy
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3

class rosact(object):
    def __init__(self):
        rospy.init_node('act')
        self._pub = rospy.Publisher('/cmd_vel_mux/input/teleop',Twist,queue_size=10)
        rospy.sleep(1)

    def write(self,linear,angular):
	while True:      	
		self._pub.publish(Twist(Vector3(linear[0],linear[1],linear[2]),
                   Vector3(angular[0],angular[1],angular[2])))
		rospy.sleep(0.01)

def main():
    act=rosact()
    act.write([0.2,0,0],[0,0,0])
    print('this shouldnt be displayed')

if __name__== '__main__':
    main()
