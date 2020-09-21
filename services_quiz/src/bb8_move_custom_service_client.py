#! /usr/bin/env python

import rospy
from services_quiz.srv import BB8CustomServiceMessage, BB8CustomServiceMessageRequest # you import the service message python classes generated from Empty.srv.
import sys

# Initialise a ROS node with the name service_client
rospy.init_node('bb8_move_custom_service_client')

rospy.wait_for_service('/move_bb8_in_square_custom')

bb8_service = rospy.ServiceProxy('/move_bb8_in_square_custom', BB8CustomServiceMessage)

bb8_object = BB8CustomServiceMessageRequest()

bb8_object.side = 2
bb8_object.repetitions = 2

result = bb8_service(2,2)
print result

bb8_object.side = 4
bb8_object.repetitions = 1
result = bb8_service(4,1)
print result
