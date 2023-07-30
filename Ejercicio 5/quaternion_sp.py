#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Quaternion
from geometry_msgs.msg import Twist

rospy.init_node('quaternion', anonymous=True)	

joint1_value = 0
joint2_value = 0
joint3_value = 0
joint4_value = 0
joint5_value = 0
joint6_value = 0

def callback(data):
	global joint1_value,joint2_value,joint3_value,joint4_value
	joint1_value = data.x
	joint2_value = data.y
	joint3_value = data.z
	joint4_value = data.w
	

sub = rospy.Subscriber("quatsub", Quaternion, callback)   
pub = rospy.Publisher('quatpub', Twist, queue_size=10)
rate = rospy.Rate(1) # 10hz

while not rospy.is_shutdown():
	twistmessaje = Twist()
	
    # Angulos lineal
	twistmessaje.linear.x = joint1_value
	twistmessaje.linear.y = joint2_value
	twistmessaje.linear.z = joint3_value
	
    # Angulos angulares
	twistmessaje.angular.x = joint4_value
	
	joint5_value = joint1_value + joint2_value + joint3_value + joint4_value
	twistmessaje.angular.y = joint5_value
	
	joint6_value = joint5_value * joint5_value
	twistmessaje.angular.z = joint6_value
	
	rospy.loginfo("lineal.x: %d", joint1_value)
	rospy.loginfo("lineal.y: %d", joint2_value)
	rospy.loginfo("lineal.z: %d", joint3_value)
	rospy.loginfo("angular.x: %d", joint4_value)
	rospy.loginfo("angular.y: %d", joint5_value)
	rospy.loginfo("angular.z: %d", joint6_value)

	pub.publish(twistmessaje)
	rate.sleep()