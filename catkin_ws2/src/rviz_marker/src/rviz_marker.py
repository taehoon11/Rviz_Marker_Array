#!/usr/bin/env python
#-*- coding:utf-8 -*-

import rospy
from visualization_msgs.msg import Marker
from std_msgs.msg import ColorRGBA
from geometry_msgs.msg import Point
from tf.transformations import quaternion_from_euler
from geometry_msgs.msg import Vector3

rospy.init_node("rviz_marker")
marker_pub = rospy.Publisher("marker", Marker, queue_size=1)
text_pub = rospy.Publisher("text", Marker, queue_size=1)

while not rospy.is_shutdown():
    rviz_points = Marker()

    rviz_points.header.frame_id = "/world"
    rviz_points.ns = "points"
    rviz_points.id = 1

    rviz_points.type = Marker.POINTS
    rviz_points.action = Marker.ADD

    rviz_points.color = ColorRGBA(1, 1, 0, 1)
    rviz_points.scale = Vector3(0.2, 0.2, 0)

    # rviz_points.points.append(Point(1, 1, 0))     # 점 하나만 넣기
    rviz_points.points.append(Point(0, 0, 0))
    rviz_points.points.append(Point(1, 5, 0))
    rviz_points.points.append(Point(1, 7, 0))

    rviz_lineslist = Marker()

    rviz_lineslist.header.frame_id = "/world"
    rviz_lineslist.ns = "linelist"
    rviz_lineslist.id = 2

    rviz_lineslist.type = Marker.LINE_LIST
    rviz_lineslist.action = Marker.ADD

    rviz_lineslist.color = ColorRGBA(1, 0, 0, 1)
    rviz_lineslist.scale.x = 0.2

    x_list = [0,1,1,3,3,5,5,0]
    y_list = [0,2,2,4,4,5,5,0]

    for i in range(len(x_list)):
        rviz_lineslist.points.append(Point(x_list[i],y_list[i],0))


#    for i in range(1,3):
#        rviz_points.points.append(Point(i, i, 0))

	
    marker_pub.publish(rviz_points)
    marker_pub.publish(rviz_lineslist)
#________________________________________________________________

