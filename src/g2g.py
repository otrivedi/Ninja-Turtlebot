import rospy
import numpy as np
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3

current_pose=[]
desired_pos=[1,1]
pub = rospy.Publisher('/cmd_vel_mux/input/teleop',Twist,queue_size=10)

def main():
    rospy.init_node('act', argv=None, anonymous=False, log_level=None, disable_rostime=False, disable_rosout=False, disable_signals=True)  
    rospy.Subscriber("odom", Odometry, callback)
    rospy.spin()
    print('Finishing')


def callback(pose_struct):
	current_pose= [pose_struct.pose.pose.position.x, pose_struct.pose.pose.position.y, pose_struct.pose.pose.orientation.z]
	delt=[desired_pos[0] - current_pose[0],desired_pos[1] - current_pose[1],desired_pos[2] - current_pose[2]]
	if not any(delt)>0.05:
		rospy.signal_shutdown('Goal reached')
	print(delt)
    	write([0.1*delt[0],0.1*delt[1],0],[0,0,0.1*delt[2]])
	

def write(linear,angular):
	pub.publish(Twist(Vector3(linear[0],linear[1],linear[2]),
                   Vector3(angular[0],angular[1],angular[2])))
	rospy.sleep(0.01)

if __name__== '__main__':
    main()

