#!/usr/bin/env python
#-*- coding:utf-8 -*-

import rospy
from visualization_msgs.msg import Marker
from std_msgs.msg import ColorRGBA
from geometry_msgs.msg import Point
from tf.transformations import quaternion_from_euler
from geometry_msgs.msg import Vector3

rospy.init_node("rviz_marker")
points_pub = rospy.Publisher("points", Marker, queue_size=1)
lines_pub = rospy.Publisher("lines", Marker, queue_size=1)

while not rospy.is_shutdown():
    rviz_points = Marker()

    rviz_points.header.frame_id = "/world"
    rviz_points.ns = "points"
    rviz_points.id = 1

    rviz_points.type = Marker.POINTS
    rviz_points.action = Marker.ADD
    rviz_points.color = ColorRGBA(1, 1, 0, 1)
    rviz_points.scale = Vector3(0.2, 0.2, 0)
    rviz_points.points.append(Point(0, 0, 0))
    rviz_points.points.append(Point(1, 3, 0))
    rviz_points.points.append(Point(6, 4, 0))

    rviz_lines = Marker()

    rviz_lines.header.frame_id = "/world"
    rviz_lines.ns = "lines"
    rviz_lines.id = 2

    rviz_lines.type = Marker.LINE_LIST
    rviz_lines.action = Marker.ADD

    rviz_lines.color = ColorRGBA(1, 0, 0, 1)
    rviz_lines.scale.x = 0.2
    x_list=[1.23,1.23,1.23,2.84,2.84,2.84,2.84,1.23,1.23,1.23,1.23,-21.3,-21.3,-21.3,-21.3,-7.1,-7.1,-7.1,-7.1,-5.36,-5.36,-5.36,-5.36,1.23]
    y_list=[-11.36,11.36,11.36,11.36,11.36,15.62,15.62,15.62,15.62,18.46,18.46,18.46,18.46,16.41,16.41,16.41,16.41,-5.68,-5.68,-5.68,-5.68,-11.36,-11.36,-11.36]



    for i in range(len(x_list)):
        rviz_lines.points.append(Point(x_list[i],y_list[i],0))
    



    points_pub.publish(rviz_points)
    lines_pub.publish(rviz_lines)
