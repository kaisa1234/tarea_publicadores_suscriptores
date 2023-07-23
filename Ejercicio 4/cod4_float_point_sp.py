#!/usr/bin/env python
# --------------publicador-suscriptor de Point----------------
import rospy
from geometry_msgs.msg import Point
from std_msgs.msg import Float64

float_value_1=0.0
float_value_2=0.0
float_value_3=0.0

def callback1(data):
	global float_value_1	
	float_value_1=data.data
	rospy.loginfo("I heard canal 1 %f", float_value_1)

def callback2(data):
	global float_value_2	
	float_value_2=data.data
	rospy.loginfo("I heard canal 2 %f", float_value_2)

def callback3(data):
	global float_value_3	
	float_value_3=data.data
	rospy.loginfo("I heard canal 3 %f", float_value_3)




def funcion():
	pub = rospy.Publisher('random_float_point', Point, queue_size=10)
	
	sub = rospy.Subscriber("random_float_1", Float64, callback1)
	sub = rospy.Subscriber("random_float_2", Float64, callback2)
	sub = rospy.Subscriber("random_float_3", Float64, callback3)  
	
	rate = rospy.Rate(1) # 1hz
	while not rospy.is_shutdown():
			
		pointmessaje = Point(float_value_1, float_value_2, float_value_3)
		pub.publish(pointmessaje)
		rate.sleep()

if __name__ == '__main__':
	rospy.init_node('cod4_float_point_sp', anonymous=True)	
	try:
		funcion()
	except rospy.ROSInterruptException:
		pass
