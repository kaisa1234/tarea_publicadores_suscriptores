#!/usr/bin/env python3
#--------------publicador de Int32--------------
import rospy
from std_msgs.msg import Int32
import random

# el codigo se identifica ante ros
rospy.init_node('cod1_int_pub', anonymous=True)
# rospy.init_node('nombre-nodo', anonymous=True)
# nombre-nodo puede ser cualquiera, 
# preferible que sea igual al nombre del codigo

# se crea el topico publicador
pub = rospy.Publisher('random_int_1', Int32, queue_size=1)
# pub = rospy.Publisher('nombre-topico', tipo-mensaje, queue_size=1)

rate = rospy.Rate(1) # 10hz --> 1/10hz=0.1s
while not rospy.is_shutdown():
    valor=random.randint(1,10)
    print(valor)
    pub.publish(valor) # se publica el valor
    # tambien se puede publicar al topico desde la terminal con:
    # rostopic pub /random_int std_msgs/Int32 '2'
    rate.sleep() # delay de 1 segundo
