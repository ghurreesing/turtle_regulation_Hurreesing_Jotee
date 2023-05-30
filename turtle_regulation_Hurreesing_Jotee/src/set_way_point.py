#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import math
from turtlesim.msg import Pose
PI = 3.1415926535897

def way_point():
    global waypoint, turtlePose
    turtlePose=None
    waypoint=[7,7]
    Kp=rospy.get_param("~kp",10)
    rospy.init_node("set_way_point")
    pub=rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=1)
    rate=rospy.Rate(30)
    rospy.Subscriber("/turtle1/pose",Pose, getPose)
    while not rospy.is_shutdown():
        message=Twist()
        if turtlePose is not None:
            e=angle()
            u=Kp*e
            message.angular.z=u
        pub.publish(message)
        rate.sleep()

def angle():
        theta_desired=math.atan2((waypoint[1]-turtlePose.y),(waypoint[0]-turtlePose.x))
        erreur=math.atan(math.tan((theta_desired-turtlePose.theta)/2))
        return erreur

def getPose(pose):
    global turtlePose
    turtlePose=pose

if __name__=="__main__":
        try:
                way_point()
        except ROSInterruptException:
                pass
