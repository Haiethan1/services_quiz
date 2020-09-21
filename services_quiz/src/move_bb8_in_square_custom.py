#! /usr/bin/env python

import rospy
from services_quiz.srv import BB8CustomServiceMessage, BB8CustomServiceMessageResponse# you import the service message python classes generated from Empty.srv.
from geometry_msgs.msg import Twist
import time

def my_callback(request):
    print "Repitions"+str(request.repetitions)#checkers
    print "Side"+str(request.side)
    response = BB8CustomServiceMessageResponse()
    square = Twist()
    
    for x in range(0, request.repetitions):
        for i in range (0, 4):
            square.linear.x = 1.0
            pub.publish(square)
            time.sleep(request.side)

            square.linear.x = 0.0
            pub.publish(square)
            time.sleep(request.side)

            square.angular.z = 1.0
            pub.publish(square)
            time.sleep(request.side)

            square.angular.z = 0.0
            pub.publish(square)
            time.sleep(request.side)
        


    square.linear.x = 0
    square.angular.z = 0
    pub.publish(square)
    response.success = True
    
    return response # the service Response class, in this case EmptyResponse
    #return MyServiceResponse(len(request.words.split())) 

rospy.init_node('move_bb8_in_square_custom') 
my_service = rospy.Service('/move_bb8_in_square_custom', BB8CustomServiceMessage , my_callback) # create the Service called my_service with the defined callback
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
rospy.spin() # maintain the service open.