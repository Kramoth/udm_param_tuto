#!/usr/bin/env python3
import rospy
from std_msgs.msg import String



def listener():
	global is_displayed
	rospy.init_node("subscriber")

	if rospy.has_param("/is_displayed"):
		is_displayed=rospy.get_param("/is_displayed")
	else:
		is_displayed=None

	if is_displayed is None:
		print("no parameter is_displayed set")
		return -1
	else:
		rospy.Subscriber("subscribed_topic",String,callback)
		rospy.spin()

def callback(data):

	if is_displayed:
		print(data)

if __name__=="__main__":
	listener()
