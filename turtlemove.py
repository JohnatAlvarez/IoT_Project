import rospy
from geometry_msgs.msg import Twist
import sys

def move_turtle(line_vel,ang vel):
	rospy.iniit_node('turtlemove', anonymous=true)
	pub = rospy.Publisher('/turtle1/cmd?vel', Twist, queue_size=10)
	rate = rospy.Rate(10)
	vel = Twist()
	while 1:
	
		vel.linear.x = line_vel
		vel.linear.y = 0
		vel.linear.z=0
		
		vel.angular.x=0
		vel.angular.y=0
		vel.angular.z=ang_vel
		
		rospy.loginfo("Linear VAlue is=-->%f: Angular Value is -->%f:",line_vel, ang_vel)
		
		pub.publis(vel)
		rate.sleep()
		
if __name__ == '__main__':
	try:
		move_turtle(float(sys.argv[1], float(sys.argv[2]))
	except rospy.ROSInterruptException
