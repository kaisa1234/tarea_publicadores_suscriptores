#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

rospy.init_node('twist', anonymous=True)	

joint1_value = 0
joint2_value = 0
joint3_value = 0
joint4_value = 0
joint5_value = 0
joint6_value = 0

def callback(data):
    global joint1_value,joint2_value,joint3_value,joint4_value,joint5_value,joint6_value
    joint1_value = data.linear.x;
    joint2_value = data.linear.y;
    joint3_value = data.linear.z;
    joint4_value = data.angular.x;
    joint5_value = data.angular.y;
    joint6_value = data.angular.z;
    

sub = rospy.Subscriber("quatpub", Twist, callback)
rate = rospy.Rate(1) # 1hz

while not rospy.is_shutdown():
    rospy.loginfo("lineal.x: %d", joint1_value)
    rospy.loginfo("lineal.y: %d", joint2_value)
    rospy.loginfo("lineal.z: %d", joint3_value)
    rospy.loginfo("angular.x: %d", joint4_value)
    rospy.loginfo("angular.y: %d", joint5_value)
    rospy.loginfo("angular.z: %d", joint6_value)
    rate.sleep()
