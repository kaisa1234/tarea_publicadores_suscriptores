#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Quaternion

rospy.init_node('quaternion_sp', anonymous=True)	

joint1_value = 0.0
joint2_value = 0.0
joint3_value = 0.0
joint4_value = 0.0
joint5_value = 0.0
joint6_value = 0.0

def callback(data):
	#rospy.loginfo("I heard %d", data.x) #como print
	global joint1_value,joint2_value,joint3_value,joint4_value
	joint1_value = data.x;
	joint2_value = data.y;
	joint3_value = data.z;
	joint4_value = data.w;
	rospy.loginfo("x: %f", joint1_value)
	rospy.loginfo("y: %f", joint2_value)
	rospy.loginfo("z: %f", joint3_value)
	rospy.loginfo("w: %f", joint4_value)

pub = rospy.Publisher('quatpub', Quaternion, queue_size=10)
sub = rospy.Subscriber("quatsub", Quaternion, callback)   
rate = rospy.Rate(1) # 10hz
while not rospy.is_shutdown():
	
	joint5_value = joint1_value+joint2_value+joint3_value+joint4_value+joint5_value
        joint6_value = joint5_value*joint5_value
	pointmessaje = Quaternion(joint1_value,joint2_value,joint3_value,joint4_value)
	pub.publish(pointmessaje)
	rate.sleep()
