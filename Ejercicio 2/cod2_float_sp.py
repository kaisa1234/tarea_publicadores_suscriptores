#!/usr/bin/env python
# --------------publicador-suscriptor de Float64--------------
# el codigo escucha al topico 'floatsub'
# Y publica al topico 'floatpub' el cuadrado de los valores que lleguen
import rospy
from std_msgs.msg import Float64

rospy.init_node('cod2_fload_sp', anonymous=True)
float_value=0.0

def callback(data):
	global float_value	
	float_value=data.data
	rospy.loginfo("I heard %f", float_value)

pub = rospy.Publisher('random_float_pub', Float64, queue_size=10)
sub = rospy.Subscriber("random_float", Float64, callback)
# publicar a floatsub desde terminal con: 
# rostopic pub /floatsub std_msgs/Float64 "data: 4.0"

rate = rospy.Rate(1) # 10hz
while not rospy.is_shutdown():
	valor=float_value*float_value
	pub.publish(valor)
	# escuchar el valor cuadrado desde terminal con:
	# rostopic echo /floatpub
	rate.sleep()
