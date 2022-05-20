#!/usr/bin/env python
import rospy
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import Bool
from yaml import safe_load_all


def callback(data):
    global stop_sign_index
    global stop_start_timer
    global pub

    stopping_radius = int(rospy.get_param("stop_sign_stopping_distance"))
    if (abs(data.pose.position.x - stop_signs[stop_sign_index][0]) < stopping_radius) and (
            abs(data.pose.position.y - stop_signs[stop_sign_index][1]) < stopping_radius):
        stop_curr_time = rospy.get_time()
        # Number of seconds the car will stop
        if stop_curr_time - stop_start_timer >= 3:
            if stop_sign_index >= len(stop_signs) - 1:
                stop_sign_index = 0
            else:
                stop_sign_index += 1
            pub.publish(False)
            rospy.loginfo("Stopping for stop sign number %s", stop_sign_index + 1)
        else:
            pub.publish(True)
    else:
        stop_start_timer = rospy.get_time()


def main():
    rospy.init_node('stop_sign_behavior')
    rospy.Subscriber("/current_pose", PoseStamped, callback)
    rospy.spin()


if __name__ == '__main__':
    stop_sign_index = 0
    stop_start_timer = 0
    stop_signs = []
    with open(rospy.get_param("stop_sign_config_file")) as stream:
        stop_sign_config = safe_load_all(stream)
        for stop_sign in stop_sign_config:
            if stop_sign:
                stop_signs.append((stop_sign['pose']['position']['x'], stop_sign['pose']['position']['y']))
    pub = rospy.Publisher('purepursuit/stop', Bool, queue_size=10)
    main()
