#!/usr/bin/env python3
# --------------publicador-suscriptor de Int32--------------
# el codigo escucha al topico 'sub'
# Y publica al topico 'pub' el cuadrado de los valores que lleguen
import rospy
from std_msgs.msg import Int32

# el codigo se identifica ante ros
rospy.init_node('cod3_int_sp', anonymous=True)	
# nombre-nodo puede ser cualquiera, 
# preferible que sea igual al nombre del codigo
int_value_1=0
int_value_2=0
 
#se crea la funcion para recibir el mensaje del topico
def callback1(data):
	global int_value_1	
	int_value_1=data.data
	rospy.loginfo("I heard canal 1 %d", int_value_1)	#print de ROS

#se crea la funcion para recibir el mensaje del topico
def callback2(data):
	global int_value_2	
	int_value_2=data.data
	rospy.loginfo("I heard canal 2 %d", int_value_2)	#print de ROS

# se crea el publicador
pub = rospy.Publisher('random_int_suma', Int32, queue_size=1)
# se suscribe al topico
sub = rospy.Subscriber("random_int_1", Int32, callback1) 
# publicar a floatsub desde terminal con: 
# rostopic pub /intsub std_msgs/Int32 "data: 4"
sub = rospy.Subscriber("random_int_2", Int32, callback2) 
# publicar a floatsub desde terminal con: 
# rostopic pub /intsub std_msgs/Int32 "data: 4"

rate = rospy.Rate(1) # 10hz --> 1/10hz = 0.1s
while not rospy.is_shutdown():
	valor=int_value_1+int_value_2
	pub.publish(valor) # se publica el valor
	# escuchar el valor cuadrado desde terminal con:
	# rostopic echo /intpub
	rate.sleep() # delay de 0.1 segundos