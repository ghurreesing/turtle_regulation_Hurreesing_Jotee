#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import math
from std_msgs.msg import Bool 
from turtlesim.msg import Pose
PI = 3.1415926535897

def way_point():
    global waypoint, turtlePose
    turtlePose=None
    waypoint=[7,7]
    Kp=rospy.get_param("~kp",10)
    Kpl=rospy.get_param("~kpl",4)
    Distance_tolerance= rospy.get_param("~distance_tolerance",5)
    rospy.init_node("test3")
    pub=rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=1)
    publisher_moving.Publisher("is_moving",Bool,queue_size=1)
    rate=rospy.Rate(30)
    rospy.Subscriber("/turtle1/pose",Pose, getPose)
    while not rospy.is_shutdown():
        flag=Bool()
        message=Twist()
        if turtlePose is not None:
            e=angle()
            u=Kp*e
            message.angular.z=u
            el=distance()
            if (el>distance_tolerance):
               flag.data=True
               v = Kpl*el
               message.linear.velocity = v
            else flag.data=False
        pub.publish(message)
        flag.data
        rate.sleep()

def angle():
        theta_desired=math.atan2((waypoint[1]-turtlePose.y),(waypoint[0]-turtlePose.x))
        erreur=math.atan(math.tan((theta_desired-turtlePose.theta)/2))
        return erreur

def distance():
    erreur_lineaire = math.sqrt((math.pow((waypoint[1]-turtlePose.y),2)) + (math.pow((waypoint[0]-turtlePose.x),2))
    return erreur_lineaire

def getPose(pose):
    global turtlePose
    turtlePose=pose

if __name__=="__main__":
        try:
                way_point()
        except ROSInterruptException:
                pass
