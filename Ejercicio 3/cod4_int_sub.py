#!/usr/bin/env python3
# --------------suscriptor de Int32----------------
import rospy
from std_msgs.msg import Int32

# el codigo se identifica ante ros
rospy.init_node('cod4_int_sub', anonymous=True)	
#rospy.init_node('nombre-nodo', anonymous=True)
# nombre-nodo puede ser cualquiera, 
# preferible que sea igual al nombre del codigo

#se crea la funcion para recibir el mensaje del topico
def callback(valor):
    int_value=valor.data
    print("El valor de la suma es:",int_value)

# se suscribe al topico
sub = rospy.Subscriber("random_int_suma", Int32, callback)

# sub = rospy.Subscriber("nombre-topico", tipo-mensaje, funcion-callback)
# el codigo int_pub.py publica al topico 'random_int'

# Lo siguiente solo es para que el codigo no se cierre

rate = rospy.Rate(1) # 1hz --> 1/1hz=1s

# en este caso el while es para que el codigo no se cierre
# pues no hace nada :v
while not rospy.is_shutdown():
    rate.sleep() # delay de 1 segundo