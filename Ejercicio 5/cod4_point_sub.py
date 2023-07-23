#!/usr/bin/env python3
# --------------suscriptor de Float64----------------
import rospy
from geometry_msgs.msg import Point
from geometry_msgs.msg import Quaternion

# el codigo se identifica ante ros
rospy.init_node('cod4_point_sub', anonymous=True)	

int_value1 = 0.0
int_value2 = 0.0
int_value3 = 0.0
int_value4 = 0.0

#se crea la funcion para recibir el mensaje del topico
def callback(data):
    global int_value1,int_value2,int_value3	
    int_value1 = data.x;
    int_value2 = data.y;
    int_value3 = data.z;
    rospy.loginfo("x: %f", int_value1)
    rospy.loginfo("y: %f", int_value2)
    rospy.loginfo("z: %f", int_value3)

pub = rospy.Publisher('quatpub', Quaternion, queue_size=10)
sub = rospy.Subscriber("random_int_point", Point, callback)  
rate = rospy.Rate(1) # 1hz
while not rospy.is_shutdown():
	
	int_value4=int_value1+int_value2+int_value3	
	pointmessaje = Quaternion(int_value1, int_value2, int_value3, int_value4)
	pub.publish(pointmessaje)
	rate.sleep()